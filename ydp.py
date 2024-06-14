# 출산양육지원사업안내 페이지 크롤러
def ydp_1page_crawler(url):
    # 정보 담을 리스트 초기화
    admin_list = []         # 관리자 ID
    category_list = []      # 카테고리 (분야)
    host_list = []          # 주최 (국가/구)
    title_list = []         # 지원사업명 (제목)
    content_list = []       # 내용
    original_url_list = []  # 원본 URL
    way_list = []           # 신청방법
    etc_list = []           # 문의처

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # h3 태그와 그 다음 ul.bu 태그를 차례로 선택하여 정보 추출
    h3_tags = soup.select('#contents > h3')
    for index, h3_tag in enumerate(h3_tags):
        try:
            # 제목 추출
            title = h3_tag.text.strip()
            title_list.append(title)

            # 해당 제목 다음에 나오는 ul.bu 태그 선택
            next_ul = h3_tag.find_next_sibling('ul', class_='bu')
            if next_ul:
                li_tags = next_ul.find_all('li')
                way_text = ""  # 신청방법 텍스트
                etc_text = ""  # 문의처 텍스트
                content_text = ""   # 내용 텍스트
                for li in li_tags:
                    text = li.text.strip()
                    if '신청방법' in text:
                        way_text = text.split(': ', 1)[1] if ': ' in text else 'N/A'  # ":" 이후의 텍스트만 가져오기
                    elif '문의' in text:
                        etc_text = text.split(': ', 1)[1] if ': ' in text else 'N/A'  # ":" 이후의 텍스트만 가져오기
                    else:
                        content_text += text + "\n"

                # 신청방법 및 문의처, 내용 추가
                way_list.append(way_text.strip())
                etc_list.append(etc_text.strip())
                content_list.append(content_text.strip())
            else:
                way_list.append('N/A')
                etc_list.append('N/A')
                content_list.append('N/A')

            # 주최 (국가/구) 및 카테고리 (분야) 추출
            content_ul = h3_tag.find_next_sibling('ul')
            if content_ul:
                text = content_ul.text.strip()
                if text.find('영등포') != -1:
                    host = 1156000000  # 영등포구 행정코드
                else:
                    host = 9000000009  # 정부 행정코드
                host_list.append(host)

                if text.find('산모') != -1:
                    category = 1  # 임신/출산
                else:
                    category = 2  # 영유아
                category_list.append(category)
            else:
                host_list.append('n/a')
                category_list.append('n/a')

            # 관리자 ID와 원본 URL 추가
            admin_id = 'teamwemmy@gmail.com'
            admin_list.append(admin_id)
            original_url_list.append(url)

        except Exception as e:
            print(f"Error occurred while processing title {index + 1}: {e}")

    # 데이터 프레임 생성
    df = pd.DataFrame({
        'admin_id': admin_list,
        'w_category_id': category_list,
        'host_id': host_list,
        'title': title_list,
        'content': content_list,
        'way': way_list,
        'etc': etc_list,
        'original_url': original_url_list  # URL은 각각의 행에 해당
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df


# 보육료 지원 안내 페이지 크롤러
def ydp_2page_crawler(url):
    # 정보 담을 리스트 초기화
    admin_list = []         # 관리자 ID
    category_list = []      # 카테고리 (분야)
    host_list = []          # 주최 (국가/구)
    title_list = []         # 지원사업명 (제목)
    content_list = []       # 내용
    original_url_list = []  # 원본 URL
    way_list = []           # 신청방법
    etc_list = []           # 문의처
    way_text = ""           # 신청방법 텍스트
    content_text = ""       # 내용 텍스트

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # h3 태그와 그 다음 ul, p, div 태그를 차례로 선택하여 정보 추출
    h3_tags = soup.select('#contents > h3')
    for index, h3_tag in enumerate(h3_tags):
        try:
            #  추출
            temp = h3_tag.string.strip()  # h3 태그의 실제 텍스트 값 추출
            if '신청' in temp:
                way_text += temp + "\n"
            else:
                content_text += temp + "\n"

            # 다음에 나오는 태그 선택
            next_tag = h3_tag.find_next_sibling(['ul', 'p', 'div', 'table'])
            if next_tag:
                # 태그 내의 텍스트 추출
                if next_tag.name == 'table':  # 만약 다음 태그가 table이라면
                    table_df = pd.read_html(str(next_tag))[0]  # table을 데이터프레임으로 변환
                    content_text += table_df.to_string(index=False) + "\n"  # 데이터프레임을 텍스트로 변환하여 추가
                else:
                    text = next_tag.get_text(strip=True)
                    if '방문' in text or '온라인' in text:
                        way_text += temp + "\n"
                    else:
                        content_text += text + "\n"

        except Exception as e:
            print(f"Error occurred while processing title {index + 1}: {e}")

    # 중복된 결과값 제거
    way_text = "\n".join(list(set(way_text.split("\n"))))

    # 신청방법 및 내용 추가
    way_list.append(way_text.strip())
    content_list.append(content_text.strip())


    # 제목 추가
    title_text = soup.select('#colgroup > article > header > div.sub_title > h2')[0].text.strip()
    title_list.append(title_text)

    # 문의처 추가
    etc_text = soup.select('#colgroup > article > footer > div > ul')[0].text.strip()
    etc_list.append(etc_text)

    # 주최 및 분야, 관리자 ID, 원본 URL 추가
    admin_id = 'teamwemmy@gmail.com'
    admin_list.append(admin_id)
    original_url_list.append(url)
    host = 9000000009  # 정부 행정코드
    host_list.append(host)
    category = 2  # 영유아
    category_list.append(category)

    # 데이터 프레임 생성
    df = pd.DataFrame({
        'admin_id': admin_list,
        'w_category_id': category_list,
        'host_id': host_list,
        'title': title_list,
        'content': content_list,
        'way': way_list,
        'etc': etc_list,
        'original_url': original_url_list  # URL은 각각의 행에 해당
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df


# 아이돌봄 서비스 안내 페이지 크롤러
def ydp_3page_crawler(url):
    # 정보 담을 리스트 초기화
    admin_list = []         # 관리자 ID
    category_list = []      # 카테고리 (분야)
    host_list = []          # 주최 (국가/구)
    title_list = []         # 지원사업명 (제목)
    content_list = []       # 내용
    original_url_list = []  # 원본 URL
    way_list = []           # 신청방법
    etc_list = []           # 문의처

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for i in range(2):  # 2번 반복
        # 제목 추가
        title_text = soup.select(f'#contents > h3:nth-child({2 + i * 5})')[0].text.strip()
        title_list.append(title_text)

        # 내용 추출
        content_text = ''
        ul_selector = f'#contents > ul:nth-child({3 + i * 5})'
        ul_content = soup.select(ul_selector)[0].text.strip()
        content_text += ul_content

        div_selector = f'#contents > div:nth-child({5 + i * 5})'
        # div 태그가 있는지 확인하고 데이터프레임으로 저장하거나 그대로 내용을 추가
        if soup.select(div_selector):
            table = soup.select(div_selector)[0]
            df_content = pd.read_html(str(table))[0]
            # 데이터프레임을 문자열로 변환하여 추가
            content_text += df_content.to_string(index=False) + '\n'
        else:
            div_content = soup.select(div_selector)[0].text.strip()
            content_text += div_content + '\n'

        ul_selector = '#contents > ul:nth-child(12)'
        ul_content = soup.select(ul_selector)[0].text.strip()
        content_text += ul_content

        content_list.append(content_text)


        # 신청방법 추가
        way_text = soup.select(f'#contents > ul:nth-child(14)')[0].text.strip()
        way_list.append(way_text)

        # 문의처 추가
        etc_text = soup.select(f'#contents > ul:nth-child(14) > li:nth-child(5)')[0].text.strip()
        exc_text = etc_text.split(': ', 1)[1] if ': ' in etc_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
        etc_list.append(exc_text)

        # 주최 및 분야, 관리자 ID, 원본 URL 추가
        admin_id = 'teamwemmy@gmail.com'
        admin_list.append(admin_id)
        original_url_list.append(url)
        host = 9000000009  # 정부 행정코드
        host_list.append(host)
        category = 2  # 영유아
        category_list.append(category)


    # 데이터 프레임 생성
    df = pd.DataFrame({
        'admin_id': admin_list,
        'w_category_id': category_list,
        'host_id': host_list,
        'title': title_list,
        'content': content_list,
        'way': way_list,
        'etc': etc_list,
        'original_url': original_url_list  # URL은 각각의 행에 해당
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df


# 다둥이 행복카드 안내 페이지 크롤러
def ydp_4page_crawler(url):
    # 정보 담을 리스트 초기화
    admin_list = []         # 관리자 ID
    category_list = []      # 카테고리 (분야)
    host_list = []          # 주최 (국가/구)
    title_list = []         # 지원사업명 (제목)
    content_list = []       # 내용
    original_url_list = []  # 원본 URL
    way_list = []           # 신청방법
    etc_list = []           # 문의처

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 제목 추가
    title_text = soup.select('#colgroup > article > header > div.sub_title > h2')[0].text.strip()
    title_list.append(title_text)

    # 내용 추가
    content_text = soup.select('#contents > p:nth-child(2)')[0].text.strip()
    content_text += soup.select('#contents > h3:nth-child(7)')[0].text.strip()
    content_text += soup.select('#contents > ul:nth-child(8) > li:nth-child(3)')[0].text.strip()
    content_text += soup.select('#contents > div > ul')[0].text.strip()
    content_list.append(content_text)

    # 신청방법 추가
    way_text = soup.select('#contents > ul:nth-child(6)')[0].text.strip()
    way_list.append(way_text)

    # 문의처 추가
    etc_text = soup.select('#contents > p:nth-child(4)')[0].text.strip()
    etc_list.append(etc_text)

    # 주최 및 분야, 관리자 ID, 원본 URL 추가
    admin_id = 'teamwemmy@gmail.com'
    admin_list.append(admin_id)
    original_url_list.append(url)
    host = 9000000009  # 정부 행정코드
    host_list.append(host)
    category = 2  # 영유아
    category_list.append(category)

    # 데이터 프레임 생성
    df = pd.DataFrame({
        'admin_id': admin_list,
        'w_category_id': category_list,
        'host_id': host_list,
        'title': title_list,
        'content': content_list,
        'way': way_list,
        'etc': etc_list,
        'original_url': original_url_list  # URL은 각각의 행에 해당
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df


# 아동수당 지원사업 안내 페이지 크롤러
def ydp_5page_crawler(url):
    # 정보 담을 리스트 초기화
    admin_list = []         # 관리자 ID
    category_list = []      # 카테고리 (분야)
    host_list = []          # 주최 (국가/구)
    title_list = []         # 지원사업명 (제목)
    content_list = []       # 내용
    original_url_list = []  # 원본 URL
    way_list = []           # 신청방법
    etc_list = []           # 문의처

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 제목 추가
    title_text = soup.select('#colgroup > article > header > div.sub_title > h2')[0].text.strip()
    title_list.append(title_text)

    # 내용 추가
    content_text = soup.select('#contents > ul:nth-child(2)')[0].text.strip()
    content_text += soup.select('#contents > p:nth-child(6)')[0].text.strip()
    content_text += soup.select('#contents > p:nth-child(8)')[0].text.strip()
    content_list.append(content_text)

    # 신청방법 추가
    way_text = soup.select('#contents > ul:nth-child(4)')[0].text.strip()
    way_list.append(way_text)

    # 문의처 추가
    etc_text = soup.select('#contents > p:nth-child(10)')[0].text.strip()
    etc_list.append(etc_text)

    # 주최 및 분야, 관리자 ID, 원본 URL 추가
    admin_id = 'teamwemmy@gmail.com'
    admin_list.append(admin_id)
    original_url_list.append(url)
    host = 9000000009  # 정부 행정코드
    host_list.append(host)
    category = 2  # 영유아
    category_list.append(category)


    # 데이터 프레임 생성
    df = pd.DataFrame({
        'admin_id': admin_list,
        'w_category_id': category_list,
        'host_id': host_list,
        'title': title_list,
        'content': content_list,
        'way': way_list,
        'etc': etc_list,
        'original_url': original_url_list  # URL은 각각의 행에 해당
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df


# 각 크롤링한 내용 한번에 합쳐서 저장
def ydp_crawler(urls):
    merged_df = pd.DataFrame()  # 모든 데이터프레임을 병합할 데이터프레임

    for url in urls:
        if url == url1:
            df = ydp_1page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url2:
            df = ydp_2page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url3:
            df = ydp_3page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url4:
            df = ydp_4page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url5:
            df = ydp_5page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print("지원하지 않는 URL입니다.")

    # CSV 파일 저장
    save_dir = '../[지역구]/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    csv_file_path = os.path.join(save_dir, f"영등포구_{today}_검색결과.csv")
    merged_df.to_csv(csv_file_path, encoding='utf-8-sig', index=False)
    print('CSV 파일 저장 완료:', csv_file_path)

    # 데이터 프레임을 JSON 형식으로 변환하여 저장
    json_data = merged_df.to_json(orient='records', force_ascii=False)
    json_file_path = os.path.join(save_dir, f"ydp_{today}_result.json")

    try:
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)
        print('JSON 파일 저장 완료:', json_file_path)
    except Exception as e:
        print('JSON 파일 저장 실패:', e)


import os
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import date
import json
import uuid
import numpy as np

# 오늘 날짜
today = date.today()

# 영등포구 복지 검색 사이트
url1 = 'https://www.ydp.go.kr/www/contents.do?key=3307&'
url2 = 'https://www.ydp.go.kr/www/contents.do?key=3891&'
url3 = 'https://www.ydp.go.kr/www/contents.do?key=3312&'
url4 = 'https://www.ydp.go.kr/www/contents.do?key=3310&'
url5 = 'https://www.ydp.go.kr/www/contents.do?key=3304&'

# 영등포구 페이지 크롤링 및 저장
urls = [url1, url2, url3, url4, url5]  # 크롤링할 페이지의 URL 리스트
ydp_crawler(urls)

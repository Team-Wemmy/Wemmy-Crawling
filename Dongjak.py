# 육아종합지원센터 페이지 크롤러
def dj_5page_crawler(url):
    # 정보 담을 리스트 초기화
    admin_list = []         # 관리자 ID
    category_list = []      # 카테고리 (분야)
    host_list = []          # 주최 (국가/구)
    title_list = []         # 지원사업명 (제목)
    field_list = []         # 지원대상
    content_list = []       # 내용
    url_list = []           # 원본 URL
    way_list = []           # 신청방법
    etc_list = []           # 문의처

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 제목 추가
    title_text = '서울동작구육아종합지원센터'
    title_list.append(title_text)

    # 주최 추가
    host_id = 1121500000  # 동작구 행정코드
    host_list.append(host_id)

    # 분야 추가
    category_id = 2  # 영유아
    category_list.append(category_id)

    # 관리자 추가
    admin_id = 'teamwemmy@gmail.com'
    admin_list.append(admin_id)

    # 원본 URL 추가
    url_list.append(url)

    # 지원대상 추가
    field_text = '동작구민(동작구 소재 직장인)으로 취학 전 아동이 있는 가정'
    field_list.append(field_text)

    # 신청방법 추가
    way_text = '서울동작구육아종합지원센터 홈페이지 https://www.dccic.go.kr 회원가입'
    way_list.append(way_text)

    # 문의 추가
    etc_text = '서울동작구육아종합지원센터 02-823-4567'
    etc_list.append(etc_text)

    # 내용 추가
    content_text = soup.select('#content > ul > li:nth-child(1)')[0].text.strip() + '\n'
    content_list.append(content_text)

    # 데이터 프레임 생성
    df = pd.DataFrame({
        'admin_id': admin_list,
        'w_category_id': category_list,
        'host_id': host_list,
        'title': title_list,
        'field': field_list,
        'content': content_list,
        'way': way_list,
        'etc': etc_list,
        'original_url': url_list  # URL은 각각의 행에 해당
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df

# 백일상 대여 페이지 크롤러
def dj_4page_crawler(url):
    # 정보 담을 리스트 초기화
    admin_list = []         # 관리자 ID
    category_list = []      # 카테고리 (분야)
    host_list = []          # 주최 (국가/구)
    title_list = []         # 지원사업명 (제목)
    field_list = []         # 지원대상
    content_list = []       # 내용
    url_list = []           # 원본 URL
    way_list = []           # 신청방법
    etc_list = []           # 문의처

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

   # 제목 추가
    title_text = soup.select('#contentDiv > div > h3')[0].text.strip()
    title_list.append(title_text)

    # 주최 추가
    host_id = 1159000000  # 동작구 행정코드
    host_list.append(host_id)

    # 분야 추가
    category_id = 2  # 영유아
    category_list.append(category_id)

    # 관리자 추가
    admin_id = 'teamwemmy@gmail.com'
    admin_list.append(admin_id)

    # 원본 URL 추가
    url_list.append(url)

    # 지원대상 추가
    field_text = soup.select('#contentDiv > div > ul > li:nth-child(2)')[0].text.strip()
    field_list.append(field_text)

    # 신청방법 추가
    way_text = '대한민국동작주식회사 https://kdongjak.co.kr/ 홈페이지 신청'
    way_list.append(way_text)

    # 문의 추가
    etc_text = soup.select('#contentDiv > div > div.page-inf > div.manager > dl > dd')[0].text.strip()
    etc_list.append(etc_text)

    # 내용 추가
    content_text = soup.select('#contentDiv > div > ul > li:nth-child(1)')[0].text.strip() + '\n'
    content_text += soup.select('#contentDiv > div > ul > li:nth-child(3)')[0].text.strip() + '\n'
    content_text += soup.select('#contentDiv > div > ul > li:nth-child(4)')[0].text.strip() + '\n'
    content_text += soup.select('#contentDiv > div > ul > li:nth-child(5)')[0].text.strip() + '\n'
    content_list.append(content_text)

    # 데이터 프레임 생성
    df = pd.DataFrame({
        'admin_id': admin_list,
        'w_category_id': category_list,
        'host_id': host_list,
        'title': title_list,
        'field': field_list,
        'content': content_list,
        'way': way_list,
        'etc': etc_list,
        'original_url': url_list  # URL은 각각의 행에 해당
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df


# 서울엄마아빠택시 페이지 크롤러
def dj_3page_crawler(url):
    # 정보 담을 리스트 초기화
    admin_list = []         # 관리자 ID
    category_list = []      # 카테고리 (분야)
    host_list = []          # 주최 (국가/구)
    title_list = []         # 지원사업명 (제목)
    field_list = []         # 지원대상
    content_list = []       # 내용
    url_list = []           # 원본 URL
    way_list = []           # 신청방법
    etc_list = []           # 문의처

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

   # 제목 추가
    title_text = soup.select('#contentDiv > div > h3')[0].text.strip()
    title_list.append(title_text)

    # 주최 추가
    host_id = 1159000000  # 동작구 행정코드
    host_list.append(host_id)

    # 분야 추가
    category_id = 2  # 영유아
    category_list.append(category_id)

    # 관리자 추가
    admin_id = 'teamwemmy@gmail.com'
    admin_list.append(admin_id)

    # 원본 URL 추가
    url_list.append(url)

    # 지원대상 추가
    field_text = soup.select('#contentDiv > div > ul > li:nth-child(3)')[0].text.strip()
    field_list.append(field_text)

    # 신청방법 추가
    way_text = soup.select('#contentDiv > div > ul > li:nth-child(15)')[0].text.strip()
    way_list.append(way_text)

    # 문의 추가
    etc_text = soup.select('#contentDiv > div > ul > li:nth-child(21)')[0].text.strip()
    etc_text = etc_text.split(':', 1)[1].strip() if ': ' in etc_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    etc_list.append(etc_text)

    # 내용 추가
    content_text = soup.select('#contentDiv > div > ul > li:nth-child(6)')[0].text.strip() + '\n'
    content_text += soup.select('#contentDiv > div > ul > li:nth-child(9)')[0].text.strip() + '\n'
    content_text += soup.select('#contentDiv > div > ul > li:nth-child(12)')[0].text.strip() + '\n'
    content_text += soup.select('#contentDiv > div > ul > li:nth-child(18)')[0].text.strip() + '\n'
    content_list.append(content_text)

    # 데이터 프레임 생성
    df = pd.DataFrame({
        'admin_id': admin_list,
        'w_category_id': category_list,
        'host_id': host_list,
        'title': title_list,
        'field': field_list,
        'content': content_list,
        'way': way_list,
        'etc': etc_list,
        'original_url': url_list  # URL은 각각의 행에 해당
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df


# 출산 페이지 크롤러
def dj_2page_crawler(url):
    # 정보 담을 리스트 초기화
    admin_list = []         # 관리자 ID
    category_list = []      # 카테고리 (분야)
    host_list = []          # 주최 (국가/구)
    title_list = []         # 지원사업명 (제목)
    field_list = []         # 지원대상
    content_list = []       # 내용
    url_list = []           # 원본 URL
    way_list = []           # 신청방법
    etc_list = []           # 문의처

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # h3 태그와 그 다음 ul.bu 태그를 차례로 선택하여 정보 추출
    h3_tags = soup.select('#contentDiv > h3')
    for index, h3_tag in enumerate(h3_tags):
        try:
            # 제목 추출
            title = h3_tag.text.strip()
            title_list.append(title)

            # 해당 제목 다음에 나오는 ul.bu 태그 선택
            next_ul = h3_tag.find_next_sibling('ul', class_='list')
            if next_ul:
                li_tags = next_ul.find_all('li')
                field_text = ""  # 지원대상 텍스트
                content_text = ""   # 내용 텍스트
                for li in li_tags:
                    text = li.text.strip()
                    if  '지원대상' in text:
                        field_text = text.split(': ', 1)[1] if ': ' in text else 'N/A'  # ":" 이후의 텍스트만 가져오기
                    elif '신청방법' in text:
                        way_text = text.split(': ', 1)[1] if ': ' in text else 'N/A'
                    elif '문의처' in text:
                        etc_text = text.split(': ', 1)[1] if ': ' in text else 'N/A'
                    else:
                        content_text += text + "\n"

                # 지원대상, 내용, 신청방법, 문의 추가
                field_list.append(field_text.strip())
                way_list.append(way_text.strip())
                etc_list.append(etc_text.strip())
                content_list.append(content_text.strip())
            else:
                field_list.append('N/A')
                way_list.append('N/A')
                etc_list.append('N/A')
                content_list.append('N/A')

            # 분야, 주최, 관리자 ID와 원본 URL 추가
            category_id = 1  # 임신/출산
            category_list.append(category_id)
            host_id = 1159000000  # 동작구 행정코드
            host_list.append(host_id)
            admin_id = 'teamwemmy@gmail.com'
            admin_list.append(admin_id)
            url_list.append(url)

        except Exception as e:
            print(f"Error occurred while processing title {index + 1}: {e}")

    # 데이터 프레임 생성
    df = pd.DataFrame({
        'admin_id': admin_list,
        'w_category_id': category_list,
        'host_id': host_list,
        'title': title_list,
        'field': field_list,
        'content': content_list,
        'way': way_list,
        'etc': etc_list,
        'original_url': url_list  # URL은 각각의 행에 해당
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df

# 임산부관리 페이지 크롤러
def dj_1page_crawler(url):
    # 정보 담을 리스트 초기화
    admin_list = []         # 관리자 ID
    category_list = []      # 카테고리 (분야)
    host_list = []          # 주최 (국가/구)
    title_list = []         # 지원사업명 (제목)
    field_list = []         # 지원대상
    content_list = []       # 내용
    url_list = []           # 원본 URL
    way_list = []           # 신청방법
    etc_list = []           # 문의처

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # h2 태그와 그 다음 ul.bu 태그를 차례로 선택하여 정보 추출
    h2_tags = soup.select('#contentDiv > h2')
    for index, h2_tag in enumerate(h2_tags):
        try:
            # 제목 추출
            title = h2_tag.text.strip()
            title_list.append(title)

            # 해당 제목 다음에 나오는 ul.bu 태그 선택
            next_ul = h2_tag.find_next_sibling('ul', class_='list')
            if next_ul:
                li_tags = next_ul.find_all('li')
                field_text = ""  # 지원대상 텍스트
                content_text = ""   # 내용 텍스트
                for li in li_tags:
                    text = li.text.strip()
                    if  '동작구민' in text:
                        field_text = text.split(': ', 1)[1] if ': ' in text else 'N/A'  # ":" 이후의 텍스트만 가져오기
                    else:
                        content_text += text + "\n"

                # 지원대상, 내용 추가
                field_list.append(field_text.strip())
                content_list.append(content_text.strip())
            else:
                field_list.append('N/A')
                content_list.append('N/A')

            # 신청방법, 문의, 분야, 주최, 관리자 ID와 원본 URL 추가
            way_text = '보건소 방문'
            way_list.append(way_text.strip())
            etc_text = soup.select('#contentDiv > div > div > div.manager > dl > dd')[0].text.strip()
            etc_list.append(etc_text.strip())
            category_id = 1  # 임신/출산
            category_list.append(category_id)
            host_id = 1159000000  # 동작구 행정코드
            host_list.append(host_id)
            admin_id = 'teamwemmy@gmail.com'
            admin_list.append(admin_id)
            url_list.append(url)

        except Exception as e:
            print(f"Error occurred while processing title {index + 1}: {e}")

    # 데이터 프레임 생성
    df = pd.DataFrame({
        'admin_id': admin_list,
        'w_category_id': category_list,
        'host_id': host_list,
        'title': title_list,
        'field': field_list,
        'content': content_list,
        'way': way_list,
        'etc': etc_list,
        'original_url': url_list  # URL은 각각의 행에 해당
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df


# 각 크롤링한 내용 한번에 합쳐서 저장
def dj_crawler(urls):
    merged_df = pd.DataFrame()  # 모든 데이터프레임을 병합할 데이터프레임

    for url in urls:
        if url == url1:
            df = dj_1page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url2:
            df = dj_2page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url3:
            df = dj_3page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url4:
            df = dj_4page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url5:
            df = dj_5page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print("지원하지 않는 URL입니다.")

    # CSV 파일 저장
    save_dir = '../[지역구]/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    csv_file_path = os.path.join(save_dir, f"동작구_{today}_검색결과.csv")
    merged_df.to_csv(csv_file_path, encoding='utf-8-sig', index=False)
    print('CSV 파일 저장 완료:', csv_file_path)

    # 데이터 프레임을 JSON 형식으로 변환하여 저장
    json_data = merged_df.to_json(orient='records', force_ascii=False)
    json_file_path = os.path.join(save_dir, f"dj_{today}_result.json")

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

# 동작구 검색 사이트
url1 = 'https://www.dongjak.go.kr/portal/main/contents.do?menuNo=200281'
url2 = 'https://www.dongjak.go.kr/portal/main/contents.do?menuNo=201590'
url3 = 'https://www.dongjak.go.kr/portal/main/contents.do?menuNo=201623'
url4 = 'https://www.dongjak.go.kr/portal/main/contents.do?menuNo=201626'
url5 = 'https://www.dccic.go.kr/index.php'

# 여러 페이지 크롤링 및 저장
urls = [url1, url2, url3, url4, url5]  # 크롤링할 페이지의 URL 리스트
dj_crawler(urls)
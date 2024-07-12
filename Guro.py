#  육아종합지원센터
def gr3_page_crawler(url):
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

    # 추가
    title_list.append('구로구육아종합지원센터')
    field_list.append('구로구민(구로구 소재 직장인)으로 취학 전 아동이 있는 가정')
    content_list.append('보육에 대한 정보제공, 상담, 전문성 강화를 위한 교육 지원 등 어린이집의 질적 성장을 지원하며 영유아와 부모, 가족과 이웃이 함께 놀이하는 문화를 조성하고, 양육역량 강화를 위한 부모교육을 지원')
    way_list.append('구로구육아종합지원센터 홈페이지 https://guroccic.guro.go.kr/ 회원가입')
    etc_list.append('구로구 육아종합지원센터 (02-859-5678)')
    category_list.append(2) # 영유아
    host_list.append(1153000000)  # 구로구 행정코드
    admin_list.append('teamwemmy@gmail.com')
    url_list.append(url)


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
def gr2_page_crawler(url):
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

    # 임산부 산전관리 추가
    title_text = soup.select('#contents > h3:nth-child(2)')[0].text.strip()
    title_list.append(title_text)
    field_text = soup.select('#contents > ul:nth-child(3) > li:nth-child(1)')[0].text.strip()
    field_text += '\n' + soup.select('#contents > ul:nth-child(3) > li:nth-child(2)')[0].text.strip()
    field_list.append(field_text)
    content_text = soup.select('#contents > ul:nth-child(4) > li:nth-child(1)')[0].text.strip()
    content_text += soup.select('#contents > ul:nth-child(4) > li:nth-child(2)')[0].text.strip()
    content_text += soup.select('#contents > ul:nth-child(4) > li:nth-child(3)')[0].text.strip()
    content_text += soup.select('#contents > ul:nth-child(4) > li:nth-child(4)')[0].text.strip()
    content_text += soup.select('#contents > ul:nth-child(4) > li:nth-child(5)')[0].text.strip()
    content_text += soup.select('#contents > ul:nth-child(4) > li:nth-child(6)')[0].text.strip()
    content_list.append(content_text)
    way_text = soup.select('#contents > ul:nth-child(4) > li:nth-child(8)')[0].text.strip()
    way_text += soup.select('#contents > ul:nth-child(4) > li:nth-child(7)')[0].text.strip()
    way_list.append(way_text)
    etc_list.append('건강증진과(02-860-2421)')
    category_list.append(1) # 임신/출산
    host_list.append(1153000000) # 구로구 행정코드
    admin_list.append('teamwemmy@gmail.com')
    url_list.append(url)

    # 신후 관리 추가
    title_text = soup.select('#contents > h3:nth-child(5)')[0].text.strip()
    title_list.append(title_text)
    field_list.append('관내주민 중 출산 후 6개월 이내 산모')
    content_text = soup.select('#contents > ul:nth-child(6)')[0].text.strip()
    content_text += '\n' + soup.select('#contents > p:nth-child(7) > strong > u')[0].text.strip()
    content_text += '\n' + soup.select('#contents > ul:nth-child(8) > li')[0].text.strip()
    content_text += '\n' + soup.select('#contents > p:nth-child(9) > strong > u')[0].text.strip()
    content_list.append(content_text)
    way_text = soup.select('#contents > ul:nth-child(10) > li')[0].text.strip()
    way_list.append(way_text)
    etc_list.append('건강증진과(02-860-2421)')
    category_list.append(1) # 임신/출산
    host_list.append(1153000000) # 구로구 행정코드
    admin_list.append('teamwemmy@gmail.com')
    url_list.append(url)

    # 열린 보건소 추가
    title_text = soup.select('#contents > h3:nth-child(5)')[0].text.strip()
    title_list.append(title_text)
    field_text = soup.select('#contents > ul:nth-child(14) > li:nth-child(1)')[0].text.strip()
    field_text = field_text.split(': ', 1)[1] if ': ' in field_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    field_list.append(field_text)
    content_text = soup.select('#contents > ul:nth-child(14) > li:nth-child(3)')[0].text.strip()
    content_text = content_text.split(': ', 1)[1] if ': ' in content_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    content_text += '\n' + soup.select('#contents > p:nth-child(15)')[0].text.strip()
    content_list.append(content_text)
    way_text = soup.select('#contents > ul:nth-child(10) > li')[0].text.strip()
    way_text += '\n' + soup.select('#contents > ul:nth-child(16) > li')[0].text.strip()
    way_list.append(way_text)
    etc_list.append('건강증진과(02-860-2421)')
    category_list.append(1) # 임신/출산
    host_list.append(1153000000) # 구로구 행정코드
    admin_list.append('teamwemmy@gmail.com')
    url_list.append(url)

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

#  다자녀 출산 지원금  페이지 크롤러
def gr1_page_crawler(url):
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

    # 추가
    title_text = soup.select('#colgroup > article > header > div.sub_info > div.sub_title > h2')[0].text.strip()
    title_list.append(title_text)
    field_text = soup.select('#contents > p:nth-child(3)')[0].text.strip()
    field_text += '\n' + soup.select('#contents > p:nth-child(5)')[0].text.strip()
    field_list.append(field_text)
    content_text = soup.select('#contents > ul > li')[0].text.strip()
    content_text += '\n' + soup.select('#contents > p:nth-child(9)')[0].text.strip()
    content_list.append(content_text)
    way_text = soup.select('#contents > p:nth-child(11)')[0].text.strip()
    way_list.append(way_text)
    etc_text = soup.select('#contents > p:nth-child(13)')[0].text.strip()
    etc_list.append(etc_text)
    category_list.append(1) # 임신/출산
    host_list.append(1153000000) # 구로구 행정코드
    admin_list.append('teamwemmy@gmail.com')
    url_list.append(url)


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

#  다자녀 출산 지원금  페이지 크롤러
def gr1_page_crawler(url):
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

    # 추가
    title_text = soup.select('#colgroup > article > header > div.sub_info > div.sub_title > h2')[0].text.strip()
    title_list.append(title_text)
    field_text = soup.select('#contents > p:nth-child(3)')[0].text.strip()
    field_text += '\n' + soup.select('#contents > p:nth-child(5)')[0].text.strip()
    field_list.append(field_text)
    content_text = soup.select('#contents > ul > li')[0].text.strip()
    content_text += '\n' + soup.select('#contents > p:nth-child(9)')[0].text.strip()
    content_list.append(content_text)
    way_text = soup.select('#contents > p:nth-child(11)')[0].text.strip()
    way_list.append(way_text)
    etc_text = soup.select('#contents > p:nth-child(13)')[0].text.strip()
    etc_list.append(etc_text)
    category_list.append(1) # 임신/출산
    host_list.append(1153000000) # 구로구 행정코드
    admin_list.append('teamwemmy@gmail.com')
    url_list.append(url)


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
def gr_crawler(urls):
    merged_df = pd.DataFrame()  # 모든 데이터프레임을 병합할 데이터프레임

    for url in urls:
        if url == url1:
            df = gr1_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url2:
            df = gr2_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url3:
            df = gr3_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print("지원하지 않는 URL입니다.")

    # CSV 파일 저장
    save_dir = '../[지역구]/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    csv_file_path = os.path.join(save_dir, f"구로구_{today}_검색결과.csv")
    merged_df.to_csv(csv_file_path, encoding='utf-8-sig', index=False)
    print('CSV 파일 저장 완료:', csv_file_path)

    # 데이터 프레임을 JSON 형식으로 변환하여 저장
    json_data = merged_df.to_json(orient='records', force_ascii=False)
    json_file_path = os.path.join(save_dir, f"gr_{today}_result.json")

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

# 구로구 검색 사이트
url1 = 'https://www.guro.go.kr/www/contents.do?key=4187&'
url2 = 'https://www.guro.go.kr/health/contents.do?key=1310&'
url3 = 'https://guroccic.guro.go.kr/'

# 여러 페이지 크롤링 및 저장
urls = [url1, url2, url3]  # 크롤링할 페이지의 URL 리스트
gr_crawler(urls)
#  출산양육 지원금 지원 페이지 크롤러
def gj_5page_crawler(url):
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
    title_text = soup.select('#content > div.view > h2')[0].text.strip()
    title_list.append(title_text)

    # 주최 추가
    host_id = 1121500000  # 광진구 행정코드
    host_list.append(host_id)

    # 분야 추가
    category_id = 1  # 임심/출산
    category_list.append(category_id)

    # 관리자 추가
    admin_id = 'teamwemmy@gmail.com'
    admin_list.append(admin_id)

    # 원본 URL 추가
    url_list.append(url)

    # 지원대상 추가
    field_text = soup.select('#content > ul > li:nth-child(2) > ul > li:nth-child(1)')[0].text.strip() + '\n'
    field_text += soup.select('#content > ul > li:nth-child(2) > ul > li:nth-child(2)')[0].text.strip() + '\n'
    field_text += soup.select('#content > ul > li:nth-child(2) > ul > li:nth-child(3)')[0].text.strip()
    field_list.append(field_text)

    # 신청방법 추가
    way_text = soup.select('#content > ul > li:nth-child(6)')[0].text.strip()
    way_list.append(way_text)

    # 문의 추가
    etc_text = soup.select('#content > div.view > div.t > dl > dd')[0].text.strip()
    etc_list.append(etc_text)

    # 내용 추가
    content_text = soup.select('#content > ul > li:nth-child(3)')[0].text.strip() + '\n'
    content_text += soup.select('#content > ul > li:nth-child(4)')[0].text.strip() + '\n'
    content_text += soup.select('#content > ul > li:nth-child(5)')[0].text.strip() + '\n'
    content_text += soup.select('#content > ul > li:nth-child(7)')[0].text.strip() + '\n'
    content_text += soup.select('#content > ul > li:nth-child(8)')[0].text.strip() + '\n'
    content_text += soup.select('#content > ul > li:nth-child(9)')[0].text.strip() + '\n'
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


# 육아종합지원센터 페이지 크롤러
def gj_4page_crawler(url):
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
    title_text = '서울광진구육아종합지원센터'
    title_list.append(title_text)

    # 주최 추가
    host_id = 1121500000  # 광진구 행정코드
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
    field_text = '광진구민(광진구 소재 직장인)으로 취학 전 아동이 있는 가정'
    field_list.append(field_text)

    # 신청방법 추가
    way_text = '서울광진구육아종합지원센터 홈페이지 https://www.gjcare.go.kr/ 회원가입'
    way_list.append(way_text)

    # 문의 추가
    etc_text = '서울광진구육아종합지원센터 02)467-1828'
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


# 서울엄마아빠택시 페이지 크롤러
def gj_3page_crawler(url):
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
    title_text = soup.select('#container > main > div.hgroup > p > span:nth-child(11)')[0].text.strip()
    title_list.append(title_text)

    # 주최 추가
    host_id = 1121500000  # 광진구 행정코드
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
    field_text = soup.select('#content > p:nth-child(2)')[0].text.strip()
    field_list.append(field_text)

    # 신청방법 추가
    way_text = soup.select('#content > p:nth-child(14)')[0].text.strip()
    way_list.append(way_text)

    # 문의 추가
    etc_text = soup.select('#cmi-deptKorNm')[0].text.strip() + '\t'
    etc_text += soup.select('#cmi-userTelno')[0].text.strip()
    etc_list.append(etc_text)

    # 내용 추가
    content_text = soup.select('#content > h2:nth-child(9)')[0].text.strip() + '\n'
    content_text += soup.select('#content > ul:nth-child(10)')[0].text.strip() + '\n'
    content_text += soup.select('#content > h2:nth-child(11)')[0].text.strip() + '\n'
    content_text += soup.select('#content > ul:nth-child(12)')[0].text.strip() + '\n'
    content_text += soup.select('#content > h2:nth-child(3)')[0].text.strip() + ':\t'
    content_text += soup.select('#content > p:nth-child(4)')[0].text.strip() + '\n'
    content_text += soup.select('#content > h2:nth-child(7)')[0].text.strip() + ':\t'
    content_text += soup.select('#content > p:nth-child(8)')[0].text.strip() + '\n'
    content_text += soup.select('#content > h2:nth-child(5)')[0].text.strip() + ':\t'
    content_text += soup.select('#content > p:nth-child(6)')[0].text.strip() + '\n'
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



# 광진아이 첫돌사진 지원 페이지
def gj_2page_crawler(url):
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
    title_text = soup.select('#container > main > div.hgroup > p > span:nth-child(11)')[0].text.strip()
    title_list.append(title_text)

    # 주최 추가
    host_id = 1121500000  # 광진구 행정코드
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
    field_text = soup.select('#content > h2:nth-child(2) > span')[0].text.strip()
    field_text = field_text.split(': ', 1)[1] if ': ' in field_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    field_text += '\n' + soup.select('#content > ul:nth-child(3) > li:nth-child(1)')[0].text.strip()
    field_text += '\n' + soup.select('#content > ul:nth-child(3) > li:nth-child(2)')[0].text.strip()
    field_list.append(field_text)

    # 신청방법 추가
    way_text = soup.select('#content > h2:nth-child(16) > span')[0].text.strip()
    way_text = way_text.split(': ', 1)[1] if ': ' in way_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    way_list.append(way_text)

    # 문의 추가
    etc_text = soup.select('#content > h2:nth-child(32) > span')[0].text.strip() + '\n'
    etc_text = etc_text.split(': ', 1)[1] if ': ' in etc_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    etc_list.append(etc_text)

    # 내용 추가
    content_text = soup.select('#content > h2:nth-child(5) > span')[0].text.strip() + '\n'
    content_text += soup.select('#content > h2:nth-child(7) > span')[0].text.strip() + '\n'
    content_text += soup.select('#content > ul:nth-child(8)')[0].text.strip() + '\n'
    content_text += soup.select('#content > h2:nth-child(12)')[0].text.strip() + '\n'
    content_text += '신청기간: 1차) 2024.02.01 ~ 03.31 / 2차) 2024.04.09 ~ 예산소진시까지\n'
    content_text += '대상자 선정일: 1차) 2024.04.03 ~ 04.07 / 2차) 2024.04.08 ~ 예산소진시까지\n'
    content_text += '지원금 청구기간: 2024.04.10 ~ 12.20'
    content_text += soup.select('#content > h2:nth-child(18) > span')[0].text.strip() + '\n'
    content_text += '1순위: 장애인(장애인 복지카드), 기초생활수급자(수급자확인서), 다문화가정(외국인등록증과 가족관계증명서 또는 주민등록등본), 다자녀가정(가족관계증명서 또는 주민등록등본)\n'
    content_text += '2순위: 1순위 외 가정 (대상자 주민등록초본과 부 또는 모의 주민등록초본)\n'
    content_text += soup.select('#content > h2:nth-child(22) > span')[0].text.strip() + '\n'
    content_text += soup.select('#content > h2:nth-child(24) > span')[0].text.strip() + '\n'
    content_text += soup.select('#content > p:nth-child(26)')[0].text.strip() + '\n'
    content_text += soup.select('#content > p:nth-child(27)')[0].text.strip() + '\n'
    content_text += soup.select('#content > p:nth-child(28)')[0].text.strip() + '\n'
    content_text += soup.select('#content > p:nth-child(29)')[0].text.strip() + '\n'
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


# 출생아 무료작명 서비스 페이지 크롤러
def gj_1page_crawler(url):
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
    title_text = soup.select('#container > main > div.hgroup > p > span:nth-child(11)')[0].text.strip()
    title_list.append(title_text)

    # 주최 추가
    host_id = 1121500000  # 광진구 행정코드
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
    field_text = soup.select('#content > h3:nth-child(2)')[0].text.strip()
    field_text = field_text.split(': ', 1)[1] if ': ' in field_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    field_list.append(field_text)

    # 신청방법 추가
    way_text = soup.select('#content > h4:nth-child(7)')[0].text.strip()
    way_text = way_text.split(': ', 1)[1] if ': ' in way_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    way_text += '\n' + soup.select('#content > h4:nth-child(6)')[0].text.strip()
    way_list.append(way_text)

    # 문의 추가
    etc_text = soup.select('#content > h3:nth-child(11)')[0].text.strip() + '\n'
    etc_text = etc_text.split(': ', 1)[1] if ': ' in etc_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    etc_list.append(etc_text)

    # 내용 추가
    content_text = soup.select('#content > h3:nth-child(3)')[0].text.strip() + '\n'
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


# 각 크롤링한 내용 한번에 합쳐서 저장
def gj_crawler(urls):
    merged_df = pd.DataFrame()  # 모든 데이터프레임을 병합할 데이터프레임

    for url in urls:
        if url == url1:
            df = gj_1page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url2:
            df = gj_2page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url3:
            df = gj_3page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url4:
            df = gj_4page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url5:
            df = gj_5page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print("지원하지 않는 URL입니다.")

    # CSV 파일 저장
    save_dir = '../[지역구]/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    csv_file_path = os.path.join(save_dir, f"광진구_{today}_검색결과.csv")
    merged_df.to_csv(csv_file_path, encoding='utf-8-sig', index=False)
    print('CSV 파일 저장 완료:', csv_file_path)

    # 데이터 프레임을 JSON 형식으로 변환하여 저장
    json_data = merged_df.to_json(orient='records', force_ascii=False)
    json_file_path = os.path.join(save_dir, f"gj_{today}_result.json")

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

# 광진구 검색 사이트
url1 = 'https://gwangjin.go.kr/portal/main/contents.do?menuNo=201542'
url2 = 'https://gwangjin.go.kr/portal/main/contents.do?menuNo=201591'
url3 = 'https://gwangjin.go.kr/portal/main/contents.do?menuNo=201702'
url4 = 'https://www.gjcare.go.kr/'
url5 = 'https://gwangjin.go.kr/portal/bbs/B0000178/view.do?optn3=200309&nttId=215821&searchGnrlzWlfare1=01&searchGnrlzWlfare2=038&menuNo=200301&pageIndex=2'

# 여러 페이지 크롤링 및 저장
urls = [url1, url2, url3, url4, url5]  # 크롤링할 페이지의 URL 리스트
gj_crawler(urls)



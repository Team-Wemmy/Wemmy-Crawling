import os
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import date
import json
import uuid
import time

# 오늘 날짜
today = date.today()

# 메인 페이지 크롤러
def ydp_page_crawler(soup, url):
    # 제목 추가
    title_text = soup.select('#contents > h3:nth-child(11)')[0].text.strip()
    title_list.append(title_text)

    # 주최 추가
    host_id = 1156000000  # 영등포구 행정코드
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
    field_text = soup.select('#contents > ul:nth-child(12) > li:nth-child(1)')[0].text.strip()
    field_text = field_text.split(': ', 1)[1] if ': ' in field_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    field_list.append(field_text)

    # 신청방법 추가
    way_text = soup.select('#contents > ul:nth-child(12) > li:nth-child(2)')[0].text.strip()
    way_text = way_text.split(': ', 1)[1] if ': ' in way_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    way_list.append(way_text)

    # 문의 추가
    etc_text = soup.select('#contents > ul:nth-child(12) > li:nth-child(6)')[0].text.strip()
    etc_text = etc_text.split(': ', 1)[1] if ': ' in etc_text else 'N/A'  # ":" 이후의 텍스트만 가져오기
    etc_list.append(etc_text)

    # 내용 추가
    content_text = soup.select('#contents > ul:nth-child(12) > li:nth-child(3)')[0].text.strip() + '\n'
    content_text += soup.select('#contents > ul:nth-child(12) > li:nth-child(4)')[0].text.strip() + '\n'
    content_text += soup.select('#contents > ul:nth-child(12) > li:nth-child(5)')[0].text.strip() + '\n'
    content_list.append(content_text)


# 영등포구 검색 사이트
url = 'https://www.ydp.go.kr/www/contents.do?key=3307&'

admin_list = []         # 관리자 ID
category_list = []      # 카테고리 (분야)
host_list = []          # 주최 (국가/구)
title_list = []         # 지원사업명 (제목)
field_list = []         # 지원대상
content_list = []       # 내용
way_list = []           # 신청방법
etc_list = []           # 문의처
url_list = []           # 크롤링한 세부 url

# URL로부터 페이지 내용 가져오기
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 메인 페이지 크롤링
ydp_page_crawler(soup, url)

# 각 세부 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(url_list))]

# 데이터 프레임 생성
df = pd.DataFrame({'unique_id': unique_id,
                   'admin_id': admin_list,
                   'w_category_id': category_list,
                   'host_id': host_list,
                   'title': title_list,
                   'field': field_list,
                   'content': content_list,
                   'way': way_list,
                   'etc': etc_list,
                   'original_url': url_list})

df.index = df.index + 1

# CSV 파일 저장 (선택 사항)
# 저장할 디렉토리 설정 / 없으면 생성
save_dir = '../[지역구]/'  # 적절한 디렉토리 경로로 수정
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# CSV 파일 저장
csv_file_path = save_dir + "영등포구_" + str(today) + '_검색결과.csv'
try:
    df.to_csv(csv_file_path, encoding='utf-8-sig', index=False)
    print('CSV 파일 저장 완료:', csv_file_path)
except Exception as e:
    print('CSV 파일 저장 실패:', e)

# 데이터 프레임을 JSON 형식으로 변환
json_data = df.to_json(orient='records', force_ascii=False)

# JSON 파일 저장
json_file_path = save_dir + "ydp_" + str(today) + '_result.json'
try:
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)
    print('JSON 파일 저장 완료:', json_file_path)
except Exception as e:
    print('JSON 파일 저장 실패:', e)

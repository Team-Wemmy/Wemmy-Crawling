# 필요한 모듈과 라이브러리
import os
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from datetime import date
import json
import uuid

# 오늘 날짜
today = date.today()

# 메인 페이지 크롤러
def geumcheon_page_crawler(soup):
    for data in soup.select('#contents > div > table > tbody > tr'):
        # 카테고리 (분야)
        cat_temp = data.select('td')[1].text.strip() if data.select('td') else 'N/A'
        # "임신/출산" 또는 "영유아" 카테고리에 해당하는 경우에만 정보를 수집
        if cat_temp in ['임신/출산', '영유아']:
            if cat_temp == '임신/출산':
                category = 1
            else:
                category = 2
            category_list.append(category)

            # 지원사업명 (제목)
            title_temp = data.select('td.p-subject > a')[0].text.strip() if data.select('td.p-subject > a') else 'N/A'
            title_list.append(title_temp)

            # 크롤링할 세부 URL
            if data.select('td.p-subject > a'):
                relative_url = data.select('td.p-subject > a')[0]['href']
                url_temp = 'https://www.geumcheon.go.kr/portal/' + relative_url
            else:
                url_temp = 'N/A'
            url_list.append(url_temp)

            # 주최 (국가/구)
            host_temp = data.select('td')[3].text.strip() if data.select('td') else 'N/A'
            if host_temp == '국가':
                host = 9000000009 # 국가 임의 행정코드
            else:
                host = 1154500000  # 금천구 행정코드
            host_list.append(host)

            # 관리자 ID
            admin_id = 'teamwemmy@gmail.com'
            admin_list.append(admin_id)

# 세부 페이지 크롤러
def geumcheon_target_page_crawler():
    for i in range(len(url_list)):
        if url_list[i] != 'N/A':  # 유효한 URL만 요청
            target_response = requests.get(url_list[i])
            target_html = target_response.text
            soup = BeautifulSoup(target_html, 'html.parser')

            # 지원사업명 (제목)
            title_temp = soup.select_one('#contents > div > table > tbody > tr:nth-child(4) > td')
            title_text = title_temp.get_text(strip=True) if title_temp else 'N/A'
            title_list[i] = title_text  # 기존 제목을 세부 페이지에서 크롤링한 제목으로 덮어쓰기

            # 지원대상
            field_temp = soup.select('#contents > div > table > tbody > tr:nth-child(5) > td')[0].text.strip() if soup.select('#contents > div > table > tbody > tr:nth-child(5) > td') else 'N/A'
            field_list.append(field_temp)

            # 내용
            content_temp = soup.select('#contents > div > table > tbody > tr:nth-child(6) > td')[0].text.strip() if soup.select('#contents > div > table > tbody > tr:nth-child(6) > td') else 'N/A'
            content_list.append(content_temp)

            # 신청방법
            way_temp = soup.select('#contents > div > table > tbody > tr:nth-child(7) > td')[0].text.strip() if soup.select('#contents > div > table > tbody > tr:nth-child(7) > td') else 'N/A'
             # 추가적인 조건: 주최가 '국가'인 경우에 대한 처리
            host_temp = host_list[i]
            if host_temp == 9000000009:
              if '복지로' in way_temp:
                  etc_temp = '보건복지상담센터(129)'
              elif '정부24' in way_temp:
                  etc_temp = '정부24(1588-2188)'
              elif 'bokjiro' in way_temp:
                  etc_temp = '보건복지상담센터(129)'
              elif '동주민센터' in way_temp:
                  etc_temp = '출생자의 주민등록주소지 읍면동 주민센터 문의'
              elif '구청' in way_temp:
                  etc_temp = '출생자의 주민등록주소지 구청 문의'
              elif '보건소' in way_temp:
                  etc_temp = '출생자의 주민등록주소지 관할 보건소 문의'
              elif 'socialser' in way_temp:
                  etc_temp = '사회서비스 콜센터(1566-3232)'
              else:
                  etc_temp = soup.select('#contents > div > table > tbody > tr:nth-child(8) > td')[0].text.strip() if soup.select('#contents > div > table > tbody > tr:nth-child(8) > td') else 'N/A'
            else:
              etc_temp = soup.select('#contents > div > table > tbody > tr:nth-child(8) > td')[0].text.strip() if soup.select('#contents > div > table > tbody > tr:nth-child(8) > td') else 'N/A'
            way_list.append(way_temp)
            etc_list.append(etc_temp)


# 금천구 맞춤복지 검색 사이트
url = 'https://www.geumcheon.go.kr/portal/selectBbsNttList.do?key=3892&id=&bbsNo=150544'
page_num = 1
last_page_reached = False

# 정보 담을 리스트 초기화
admin_list = []         # 관리자 ID
category_list = []      # 카테고리 (분야)
host_list = []          # 주최 (국가/구)
title_list = []         # 지원사업명 (제목)
field_list = []         # 지원대상
content_list = []       # 내용
way_list = []           # 신청방법
etc_list = []           # 문의퍼
url_list = []           # 크롤링한 세부 url

# 크롤링 걸린 시간
tik = time.time()

# 페이지가 존재할 때까지 반복
while not last_page_reached:
    page_url = url + '&pageIndex=' + str(page_num)
    response = requests.get(page_url)

    # 페이지 존재 확인 (없으면 break)
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, 'html.parser')

    # 더이상 추가 데이터 없는지 확인
    if not soup.select('#contents > div > table > tbody > tr'):
        break

    # 정보 수집
    geumcheon_page_crawler(soup)
    page_num += 1

# 크롤링 종료
print("---{} seconds done---".format(time.time() - tik))

# 메인 페이지 종료 이후, 세부 페이지 크롤링
geumcheon_target_page_crawler()

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
save_dir = '../[지역구]/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# CSV 파일 저장
csv_file_path = save_dir + "금천구_" + str(today) + '_검색결과.csv'
try:
    df.to_csv(csv_file_path, encoding='utf-8-sig')
    print('CSV 파일 저장 완료:', csv_file_path)
except Exception as e:
    print('CSV 파일 저장 실패:', e)

# 데이터 프레임을 JSON 형식으로 변환
json_data = df.to_json(orient='records', force_ascii=False)

# JSON 파일 저장
json_file_path = save_dir + "geumcheon_" + str(today) + '_result.json'
try:
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)
    print('JSON 파일 저장 완료:', json_file_path)
except Exception as e:
    print('JSON 파일 저장 실패:', e)

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
            if host_list[i] == 9000000009:  # 주최가 '국가'인 경우
                field_temp = field_temp.replace('금천구', '').strip()  # 금천구 관련 문구 제거
            field_list.append(field_temp)

            # 내용
            content_temp = soup.select('#contents > div > table > tbody > tr:nth-child(6) > td')[0].text.strip() if soup.select('#contents > div > table > tbody > tr:nth-child(6) > td') else 'N/A'
            # "-"가 포함된 경우 앞에서 한 줄 띄우기
            content_temp = content_temp.replace('-', '\n-')
            # ◦ 는 앞에서 한 줄 띄우기
            content_temp = content_temp.replace('◦', '\n◦')
            # * 는 앞에서 한 줄 띄우기
            content_temp = content_temp.replace('*', '\n*')
            # ※ 는 앞에 한 줄 띄우기
            content_temp = content_temp.replace('※', '\n※')
            #
            if '유아학비' in title_text:
                content_temp = '- 국공립: 유아학비(80,000원) / 방과후 과정(50,000원)' + '\n' +'- 사립: 유아학비(260,000원) /  방과후 과정(70,000원)'
            elif '가정양육수당' in title_text:
                content_temp = '- 1~11개월: 200,000원 / 12~23개월: 150,000원 / 24~86개월 미안: 100,000원' + '\n' +'※ 유의사항 : 출생일 포함 60일 이내 양육수당을 신청하는 경우에만 출생월로 소급하여 지원(단, 친생부인의 허가청구와 관련하여 소요된 기간은 제외함)'
            elif '시간제 어린이집' in title_text:
                content_temp = '- 어린이집, 유치원 등을 이용하지 않고 영아수당(현금) 또는 양육수당을 수급 중인 6~36개월 미만의 영아' + '\n' +'- 이용시간: 월 최대 80시간' + '\n' +'- 이용단가: 4,000원/시간\n지원: 3,000원 / 본인부담: 1,000원'
            elif '국가필수예방접종' in title_text:
                content_temp = '◦ 무료접종\n- BCG(피내 주사) 생후 3주 이후~한달 이내' + '\n' +'- 디프테리아, 파상풍, 백일해 생후 2,4,6개월, 15~18개월, 만4~6세, 만12세' + '\n' +'- 뇌수막염(hib) 폐렴구균 생후 2,4,6, 12~15개월 ' + '\n' +'- 소아마비 생후 2,4,6개월, 만4~6세 ' + '\n' +'- B형간염 생후 0,1,6개월 ' + '\n' +'- 수두 생후 12~15개월 ' + '\n' +'- 홍역, 볼거리, 풍진 생후 12~15개월, 만4~6세 ' + '\n' +'- 일본뇌염 사백신 (1,2차) 생후 12~15개월 사이 / (3차) 2차 접종 후 1년 후 / (4차) 만6세 / (5차)만12세' + '\n' +' 일본뇌염 생백신 (1차) 생후 12~23개월 사이 / (2차) 1차 접종 후 1년 후 / (3차) 만6세 ' + '\n' +'- A형간염 생후 12~36개월 사이 2회 접종 / 1차, 2차 접종간격 6~12개월 ' + '\n' +'- 인플루엔자 6개월~만12세(매년 1회 접종, 처음 접종 시 1달 간격으로 2회 접종) ' + '\n' +'- 자궁경부암(HPV) 만12세 ~17세 여성청소년, 연령별 2~3회 접종 / 2023년 대상 : 2005.1.1~2011.12.31 출생아 ' + '\n' +'- 로타바이러스생후 2~6개월 (로타릭스 2회 또는 로타텍5회)'
            elif '꿈나래통장' in title_text:
                contnet_temp = '- 구분: 생계·의료급여 수급자\n- 저축액: 5만 / 7만 / 10만' + '\n' +'- 지원금: 5만 / 7만 / 10만' + '\n' +'- 저축기간: 3년 또는 5년\n- 구분: 주거·교육급여 수급자 및 비수급자' + '\n' +'- 저축액: 5만 / 7만 / 10만 / 12만' + '\n' +'- 지원금: 2.5만 / 3.5만 / 5만 / 6만\n- 저축기간: 3년 또는 5년'
            elif '임신준비' in title_text:
                content_temp = '- 신체검사: 혈압측정' + '\n' +'◦ 검진항목' + '\n' +'- 공통: CBC(일반혈액검사) / 간기능검사 및 신장기능 검사 / B형간염검사, 매독, AIDS' + '\n' +'- 남: 정자검사(남녀임신준비지원사업 위탁기관)' + '\n' +'- 여: 난소기능검사 / 풍진검사 / 갑상선기능검사'
            elif '출산축하금 지급(금천구)' in title_text:
                content_temp = '- 2021.12.31 이전 출생아: 첫째아(30만원) / 둘째아(50만원) / 셋째아(70만원) / 넷째아 이상(100만원)' + '\n' +'- 2022.01.01 이후 출생아: 첫째아(-) / 둘째아(-) / 셋째아(50만원) / 넷째아 이상(100만원)' + '\n' +'※ 22.1.1. 이후 출생아' + '\n' +'- 첫째아, 둘째아 → 첫만남이용권으로 지원' + '\n' +' - 셋째아, 넷째아 이상 → 첫만남이용권 + 금천구 출산축하금 '
            elif '산모.신생아 건강관리 지원' in title_text:
                content_temp = '◦ 정부형' + '\n' +'1. 일반지원: 기준 중위소득 150%이하' + '\n' +'2. 예외지원: 둘째아 이상 출산가정 / 희귀난치성질환 산모 / 장애인 산모 및 장애신생아 / 셋째아 이상 출산가정 / 새터민 산모 / 결혼이민 산모 / 미혼모 산모(만24세이하) / 쌍태아 이상 출산가정 / 중위소득 150%초과 출산가정' + '\n' +'- 내용: 기초생활보장 해산급여 수급자 및 긴급복지 해산비 수급자 중복지원 가능 / 태아 유형, 출산 순위, 서비스 기간 선택 등에 따라 바우처 지원기간과 지원금 차등화 / 본인부담금 있음 / 중위소득 150% 초과 출산가정 (단축, 표준만 가능)\n◦ 서울형\n3. 서울형: 자격확인대상자 / 기초생활수급자 / 차상위계층 / 비혼모 (단축, 포준형만 지원)' + '\n' +'- 내용: 서비스 이용 본인부담금의 90% 지원\n◦ 지원 서비스 : 산모의 산후 건강관리나 신생아 관리를 위하여 가정방문, 서비스 이용권을 지급 (산모식사, 신생아 돌보기 등)'
            elif '첫만남이용권' in title_text:
                content_temp = '- 지원금액: 출생아 당 200만원 바우처 (국민행복카드)' + '\n' +'- 사용처: 유흥 및 사행업종, 마사지 등 위생업종 (이미용실 제외), 레저 등 관련 유형으로 분류된 업종 등을 제외한 전 업종 (온라인 구매 포함) 사용' + '\n' +'-사용기간: 아동출생일 (주민등록 상)로부터 1년 (사용기간 종료일 익일 0시부터 미사용 포인트 자동소멸)' + '\n' +'※ 단, 지급결정 처리기간(30일) 및 국민행복카드 신규 발급 시 소요시간 고려하여 사용종료일 이전 여유있게 신청 필요 (사용기간이 신청일 기준 1년이 아닌 출생일 기준 1년임을 유의)'
            elif '난임부부' in title_text:
                content_temp = '◦ 지원범위 : 시술비 중 본인일부 및 전액본인부담금, 비급여 3종(배아동결비, 유산방지제 및 착상보조제)' +'\n' +'◦ 내용' + '\n' +'- 체외수정: 신선배아 1~9회 / 만 44세 이하 (최대 110만원) / 만 45세 이상 (최대 90만원)' + '\n' +'- 체외수정: 동결배아 1~7회 / 만 44세 이하 (최대 50만원) / 만 45세 이상 (최대 40만원)' + '\n' + '- 인공수정 1~5회 / 만 44세 이하 (최대 30만원) / 만 45세 이상 (최대 20만원)' +'\n' + '* 용어설명' + '\n' +'- 체외수정 : 과배란 유도, 난자를 채취하여 난자세포질내 정자 직접 주입술' + '\n' +'- 신선배아 : 체외에서 수정을 한 후 3∼5일간 배양한 배아' +'\n'+'- 동결배아 : 동결 보존된 배아 '+'\n'+'- 인공수정 : 남자의 정자를 처리하여 여성의 자궁강 내로 직접 주입해주는 시술'
            content_list.append(content_temp)

            # 신청방법
            way_temp = soup.select('#contents > div > table > tbody > tr:nth-child(7) > td')[0].text.strip() if soup.select('#contents > div > table > tbody > tr:nth-child(7) > td') else 'N/A'
            # 추가적인 조건: 주최가 '국가'인 경우에 대한 처리
            if host_list[i] == 9000000009:
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
            if '서울아기 건강첫걸음 사업' in title_text:
                way_temp = '인터넷: 서울시임신 출산정보센터신청(https://seoul-agi.seoul.go.kr)\n전화신청 또는 보건소 방문'
                etc_temp = '서울시임신출산정보센터(02-2133-9489)'
            if '유아학비' in title_text:
                etc_temp = '서울특별시남부교육지원청(☎2165-0305), 교육부0079에듀콜 (☎1544-0079)'

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

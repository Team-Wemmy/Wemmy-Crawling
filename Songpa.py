#  육아종합지원센터
def sp5_page_crawler(url):
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
    title_list.append('서울송파구육아종합지원센터')
    field_list.append('송파구민(송파구 소재 직장인)으로 취학 전 아동이 있는 가정')
    content_list.append('송파구 보육 및 양육에 관한 정보의 수집·제공 및 보육교직원·부모상담 등을 제공')
    way_list.append('서울송파구육아종합지원센터 홈페이지 https://www.spscc.or.kr/ 회원가입')
    etc_list.append('서울송파구육아종합지원센터 (02-449-0505)')
    category_list.append(2) # 영유아
    host_list.append(1171000000)  # 송파구 행정코드
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

#  행복수유
def sp4_page_crawler(url):
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
    title_list.append('찾아가는 행복수유 지원사업')
    field_list.append('서울시 거주, 출산 후 8주 이내 모유수유를 원하는 송파구 산모')
    content_text = (
        '모유수유 전문가 과정을 이수한 모유수유 매니저의 가정방문을 통한 1:1 맞춤형 유방울혈 관리 및 모유수유 교육, 상담'
        '\n- 지원횟수: 1인당 최대 2회(무료)'
        '\n-> 예산범위에 한하며 예산 조기 소진시 중단될 수 있습니다.'
    )
    content_list.append(content_text)
    way_list.append('온라인 접수(서울시 임신출산 정보센터 https://seoul-agi.seoul.go.kr)')
    etc_list.append('생애건강과 산모건강증진팀 (02-2147-5149)')
    category_list.append(2) # 영유아
    host_list.append(1171000000)  # 송파구 행정코드
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

#  영양 플러스 사업
def sp3_page_crawler(url):
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
    title_list.append('영양플러스')
    field_text = (
        '송파구민 중 아래 3가지 모두를 만족한 사람 중 우선순위에 따라 선정'
        '\n- 대상자 기준 임산부, 출산수유부, 66개월 이하의 영유아'
        '\n- 소득 기준 기준 중위소득의 80% 이하 가정(건강보험료 기준금액 참조)'
        '\n-> 가구원 수는 주민등록등본을 기준으로 하되 생계를 같이하는 2촌이내 직계존비속으로 한정'
        '\n- 영양적위험요인 빈혈, 저체중, 저신장 중 한가지 이상 보유자'
        '\n-> 최종대상자 선정: 선정기준 만족여부를 판단한 후 개별 통보'
    )
    field_list.append(field_text)
    content_text = (
        '1. 사업내용'
        '\n- 대상자별 맞춤 보충식품 제공'
        '\n- 영양교육 및 상담서비스 제공(월 1회 이상)'
        '\n- 영양상담 및 보충식품 이용상황 점검을 위한 가정방문'
        '\n- 주기적인 영양위험요인 조사(영양평가)'
        '\n2. 구비서류'
        '\n- 주민등록본(최근 3개월 이내)'
        '\n- 건강보험증'
        '\n- 건강보험료납입증명서 (최근 3개월 이상 포함)'
        '\n-> 가구당 건강보험증이 2종 이상일 경우 각각의 납입증명서 제출'
        '\n-> 군인의 경우 1년 고지된 금액의 납부확인서 제출'
        '\n- 임산부: 산모수첩(담당자 확인)'
        '\n- 기타가능서류: 기초생활보장대상 증명서, 한부모 증명서, 육아휴직 증명서'
    )
    content_list.append(content_text)
    way_text = (
        '- 신청기간: 연중수시'
        '\n- 신청방법: 전화로 대기등록 02)2147-4852~3'
        '\n- 소득 기준 기준 중위소득의 80% 이하 가정(건강보험료 기준금액 참조)'
        '\n- 서류접수 및 대상자평가: 매월1회 (대기 등록자에 접수 평가 일정공지)'
        '\n- 장소: 장지동 송파산모건강증진센터 2층 영양플러스실'
    )
    way_list.append(way_text)
    etc_list.append('송파산모건강증진센터 2층 영양플러스실 (02-2147-4852~3)')
    category_list.append(2) # 영유아
    host_list.append(1171000000)  # 송파구 행정코드
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


#  신생아 청각선별검사
def sp2_page_crawler(url):
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
    title_list.append('신생아 청각선별검사')
    field_list.append('송파구에 주소지를 둔 가구의 신생아')
    content_text = (
        '1. 지원내용'
        '\n- 신생아 청각선별검사비 외래검사시 본인부담금 지원(5,000원~25,000원) / 진료비는 지원에서 제외'
        '\n- 청각선별검사결과 재검(refer)으로 판정된 후 난청 확인 검사를 받은 경우 확진검사비(7만원내)지원 (ABR 본인 부담금)'
        '\n2. 신청기간'
        '\n- 출생일 기준 1년 이내'
        '\n3. 검사시기'
        '\n- 출생후 1개월 이내 (단, 신생아중환자실에 5일 이상 입원한 신생아는 기간 제한없이 검사 가능)'
        '\n- 선별검사에서 재검(refer)이 나온 경우 : 생후 3개월 이내에 난청확진 검사 시행'
        '\n4. 난청 확진검사 가능 기관 현황'
        '\n- 서울아산병원 이비인후과(02-3010-3691)'
        '\n5. 구비서류'
        '\n- 지원신청서, 검사비 영수증, 세부내역서, 검사결과지, 보호자 통장사본 각1부, 보호자 신분증'
    )
    content_list.append(content_text)
    way_text = soup.select('#contents > p:nth-child(8)')[0].text.strip()
    way_list.append(way_text)
    etc_list.append('산모건강증진센터 (02-2147-5023)')
    category_list.append(2) # 영유아
    host_list.append(1171000000)  # 송파구 행정코드
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

#  임산부 관리
def sp1_page_crawler(url):
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

    # 임신부 건강관리
    title_list.append('임신부 건강관리')
    field_list.append('송파구 임산부')
    content_text = (
        '1. 엽산제 및 철분제 제공'
        '\n- 엽산제: 임신초기~12주까지'
        '\n- 철분제: 20주~분만전까지(5개월 분할지급 / 16주부터 지원 가능)'
        '\n- 장소: 송파산모건강증진센터'
        '\n2. 임산부 검사'
        '\n- 검사명: 임신초기검사(혈액검사) / 시기: 임신초기~  / 검사시간: 평일(오전 09시~18시, 점심시간 12시~13시 제외)'
        '\n- 검사명: 기형아검사(쿼드검사) / 시기: 16~18주 / 검사 예약: 02-2147-3741'
        '\n- 검사명: 임신성 당뇨검사(빈혈검사 포함) / 시기: 24~28주 / 검사 예약: 02-2147-3741'
        '\n- 검사명: 막달검사(혈약 및 소변검사) / 시기: 35주 전후 / 검사 예약: 02-2147-3741'
        '\n- 장소: 송파산모건강증진센터'
        '\n3. 유축기 대여'
        '\n- 대여기간: 6주 (출산 후 신청 후 2주 대기)'
        '\n- 장소: 송파산모건강증진센터'
        '\n- 문의: 02-2147-3742'
    )
    content_list.append(content_text)
    way_list.append('- 송파산모건강증진센터 방문\n평 일 : 09시~18시, 점심시간(12시~13시 제외)')
    etc_list.append('송파산모건강증진센터(02-2147-3741)')
    category_list.append(1) # 임신/출산
    host_list.append(1171000000)  # 송파구 행정코드
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
def sp_crawler(urls):
    merged_df = pd.DataFrame()  # 모든 데이터프레임을 병합할 데이터프레임

    for url in urls:
        if url == url1:
            df = sp1_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url2:
            df = sp2_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url3:
            df = sp3_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url4:
            df = sp4_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url5:
            df = sp5_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print("지원하지 않는 URL입니다.")

    # CSV 파일 저장
    save_dir = '../[지역구]/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    csv_file_path = os.path.join(save_dir, f"송파구_{today}_검색결과.csv")
    merged_df.to_csv(csv_file_path, encoding='utf-8-sig', index=False)
    print('CSV 파일 저장 완료:', csv_file_path)

    # 데이터 프레임을 JSON 형식으로 변환하여 저장
    json_data = merged_df.to_json(orient='records', force_ascii=False)
    json_file_path = os.path.join(save_dir, f"sp_{today}_result.json")

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

# 송파구 검색 사이트
url1 = 'https://www.songpa.go.kr/ehealth/contents.do?key=4568&'
url2 = 'https://www.songpa.go.kr/ehealth/contents.do?key=4571&'
url3 = 'https://www.songpa.go.kr/ehealth/contents.do?key=5306&'
url4 = 'https://www.songpa.go.kr/ehealth/contents.do?key=6071&'
url5 = 'https://www.spscc.or.kr/'

# 여러 페이지 크롤링 및 저장
urls = [url1, url2, url3, url4, url5]  # 크롤링할 페이지의 URL 리스트
sp_crawler(urls)


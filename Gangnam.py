#  가정방문 건강관리
def gn3_page_crawler(url):
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
    title_list.append('생애 초기 건강관리사업')
    field_list.append('관내 임산부, 2세 이하 영유아')
    content_text = (
        '1. 방문인력: 영유아 건강 간호사'
        '\n2. 일시: 연중'
        '\n3. 보편 방문'
        '\n- 대상: 출산 후 4주 이내(최대 6주) 가정의 산모 및 신생아'
        '\n- 방법: 출산 직후 ~ 출산 후 최대 6주 이내에 1회 가정 방문 서비스'
        '\n- 내용: 산모 건강사정(유방/유두, 오로 등), 산후 우울 및 양육 스트레스, 신생아 건강평가, 양육역량 향상(수유, 달래기, 수면문제, 부모역할 등), 예방접종 및 영유아 검진 정보제공 등'
        '\n4. 지속 방문'
        '\n- 대상: 고위험 가구 임산부 및 영유아'
        '\n- 방법: 임신 20주 이내부터 방문해 아이가 2세가 될 때까지 지속 가정 방문 서비스'
        '\n- 내용: 산모 및 영유아 건강관리, 가족 파트너십 및 양육역량 강화, 지역사회 보건 및 복지 자원 연계 등'
        '\n※사업기준에 따라 기본방문 또는 지속방문이 결정됩니다.'
    )
    content_list.append(content_text)
    way_list.append(
        '- 전화신청 및 보건소 방문'
        '\n- 전화: 문의처 확인'
        '\n- 보건소: 평 일 : 09시~18시, 점심시간(12시~13시 제외)')
    etc_list.append('영유아 건강 간호사(02-3423-7058,7166,7167,7170)')
    category_list.append(1) # 임신츌선
    host_list.append(1168000000)  # 강남구 행정코드
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
def gn2_page_crawler(url):
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
    field_list.append('강남구 임산부')
    content_text = (
        '1. 엽산제 및 철분제 제공'
        '\n- 엽산제: 임신 12주까지'
        '\n- 철분제: 16주~분만전까지(수서분소에서도 가능)'
        '\n- 장소: 보건소 1층 사랑맘건강센터'
        '\n2. 임산부 검사'
        '\n- 검사명: 임신초기검사 / 시기: ~12주 이내 / 검사내용: 풍진 항체검사, 모성검사(혈액 및 소변검사) / 검사시간: 평일(오전 09시~18시, 점심시간 12시~13시 제외)'
        '\n- 검사명: 기형아검사 / 시기: 16~18주 / 검사내용: 쿼드검사 / 검사시간: 평일 수요일 오후(사전예약필수)'
        '\n- 검사명: 임신성 당뇨검사 / 시기: 24~28주 / 검사내용: 2시간 금식 후 보건소에서 당뇨시약 마시고 1시간 후 채혈/ 검사시간: 평일(오전 09:00~10:30) / 결과지 수령일: 검사후 1주일 뒤 (인터넷 출력 가능)'
        '\n- 장소: 보건소 1층 사랑맘건강센터'
        '\n3. 임산부 구강검진 및 상담'
        '\n- 무료 구강검진 및 교육 실시'
        '\n- 장소: 보건소 1층 구강보건실'
        '\n- 구강보건실(02-3423-7218)'
        '\n4. 구비서류'
        '\n- 신분증, 출산예정일 기재된 산모수첩이나 임신확인서'
        '\n※ 첫 방문 시에는 반드시 임산부 본인이 직접 방문할 것'
    )
    content_list.append(content_text)
    way_list.append('- 보건소 방문\n평 일 : 09시~18시, 점심시간(12시~13시 제외)')
    etc_list.append('모자보건실(02-3423-7222)')
    category_list.append(1) # 임신/출산
    host_list.append(1168000000)  # 강남구 행정코드
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


#  육아종합지원센터
def gn1_page_crawler(url):
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
    title_list.append('서울강남구육아종합지원센터')
    field_list.append('강남구민(강남구 소재 직장인)으로 취학 전 아동이 있는 가정')
    content_list.append('강남구 영유아의 가정과 양육자에게 육아관련 정보 제공과 상담 및 교육, 발달지원, 놀이실, 체험프로그램, 시간제보육 서비스, 놀잇감 대여 등을 통해 가정양육을 지원')
    way_list.append('서울강남구육아종합지원센터 홈페이지 https://www.gncare.go.kr/main/index_par.php 회원가입')
    etc_list.append('서울강남구육아종합지원센터 (02-546-1736)')
    category_list.append(2) # 영유아
    host_list.append(1168000000)  # 강남구 행정코드
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
def gn_crawler(urls):
    merged_df = pd.DataFrame()  # 모든 데이터프레임을 병합할 데이터프레임

    for url in urls:
        if url == url1:
            df = gn1_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url2:
            df = gn2_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url3:
            df = gn3_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print("지원하지 않는 URL입니다.")

    # CSV 파일 저장
    save_dir = '../[지역구]/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    csv_file_path = os.path.join(save_dir, f"강남구_{today}_검색결과.csv")
    merged_df.to_csv(csv_file_path, encoding='utf-8-sig', index=False)
    print('CSV 파일 저장 완료:', csv_file_path)

    # 데이터 프레임을 JSON 형식으로 변환하여 저장
    json_data = merged_df.to_json(orient='records', force_ascii=False)
    json_file_path = os.path.join(save_dir, f"gn_{today}_result.json")

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

# 강남구 검색 사이트
url1 = 'https://www.gncare.go.kr/main/index_par.php'
url2 = 'https://health.gangnam.go.kr/content/932/view.do?mid=419-554-T&cid=&lang=ko'
url3 = 'https://health.gangnam.go.kr/content/1090/view.do?mid=419-1090&lang=ko'

# 여러 페이지 크롤링 및 저장
urls = [url1, url2, url3]  # 크롤링할 페이지의 URL 리스트
gn_crawler(urls)

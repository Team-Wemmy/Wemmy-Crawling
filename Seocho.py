#  육아종합지원센터
def sh4_page_crawler(url):
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
    title_text = soup.select('#wrap > header > div.header-bottom > h1 > a')[0].text.strip()
    title_list.append(title_text)
    field_list.append('서초구민(서초구 소재 직장인)으로 취학 전 아동이 있는 가정')
    content_list.append('서초구의 영유아와 부모, 어린이집에 전문적 보육정보와 교육서비스를 제공')
    way_list.append('서울서초구육아종합지원센터 홈페이지 https://www.gwanak.go.kr/site/educare/main.do 회원가입')
    etc_list.append('서울서초구 육아종합지원센터 (02-598-9342)')
    category_list.append(2) # 영유아
    host_list.append(1165000000)  # 서초구 행정코드
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


#  유축기 페이지 크롤러
def sh3_page_crawler(url):
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
    title_text = soup.select('#contents > h4')[0].text.strip()
    title_list.append(title_text)
    field_text = soup.select('#contents > div > ul > li:nth-child(2) > div > table > tbody > tr:nth-child(1) > td.aleft')[0].text.strip()
    field_list.append(field_text)
    content_text = '- 신청 시기: 출산 후 3개월 이내' +'\n' +'- 유축기 보유수량: 서초구 보건소(35대), 방배보건지소(19대), 서초모자보건지소(59대)'
    content_text += '\n' + '- 대여기간: 기본 30일 + 연장신청 30일 추가 가능 (최대 2개월)' +'\n' + '- 연장방법: 반납일 일주일전 재연장 신청 (※ 기간 내 연장 미신청 시 연장 불가)'
    content_text += '\n' + '- 수령/반납: 반드시 방문 수령 및 방문 반납만 가능' + '\n' +'- 비고: 소모품(깔대기,튜브,젖병 1set) 무상 지원'
    content_text += '\n' + '- 산모 신분증 / 대리인 신분증(대리인 신청시) '
    content_list.append(content_text)
    way_text = '- 인터넷 사전예약 필수' + '\n' +'- 신청방법 : 건강부모e음 회원가입 → 정보/원스톱행정 →유축기대여(신청) → 유축기 수령 가능한 곳 지정하여 대여신청하기- 서초구 보건소, 방배보건지소, 서초모자보건지소 중 1곳 지정하여 대여 원하는 날짜 선택 신청'
    way_text += '\n' + '* 선정방법 : 선착순' +'\n'+ '※ 신청일로부터 7일이내 미수령시 자동 취소' +'\n' +'- 건강부모e음 홈페이지: https://parents.seocho.go.kr/site/seochobogun/main.do'
    way_list.append(way_text)
    etc_text = soup.select('#contents > div > ul > li:nth-child(3)')[0].text.strip()
    etc_text = etc_text.replace('문 의', '').strip()
    etc_list.append(etc_text)
    category_list.append(1) # 임신/출산
    host_list.append(1165000000) # 서초구 행정코드
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


#  모유수유  페이지 크롤러
def sh2_page_crawler(url):
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

    # 추가 모유 수유
    title_text = soup.select('#contents > h4:nth-child(1)')[0].text.strip()
    title_list.append(title_text)
    field_text = soup.select('#contents > div:nth-child(2) > ul > li:nth-child(1)')[0].text.strip()
    field_text = field_text.strip().split(': ', 1)[1] if field_text else 'N/A'
    field_list.append(field_text)
    content_text = soup.select('#contents > div:nth-child(2) > ul > li:nth-child(2)')[0].text.strip()
    content_text += '\n' + soup.select('#contents > div:nth-child(2) > ul > li:nth-child(3)')[0].text.strip()
    content_text += '\n' + soup.select('#contents > div:nth-child(2) > ul > li:nth-child(4)')[0].text.strip()
    content_list.append(content_text)
    way_list.append('- 건강부모e음 https://parents.seocho.go.kr/site/seochobogun/main.do 회원가입 후 건강부모교육에서 해당강좌신청'+'\n'+'※ 반드시 사전 예약 필요')
    etc_text = soup.select('#contents > div:nth-child(2) > ul > li:nth-child(6)')[0].text.strip()
    etc_text = etc_text.replace('문 의', '').strip()
    etc_list.append(etc_text)
    category_list.append(1) # 임신/출산
    host_list.append(1165000000) # 서초구 행정코드
    admin_list.append('teamwemmy@gmail.com')
    url_list.append(url)

    # 추가 가정방문 모유 수유
    title_text = soup.select('#contents > h4:nth-child(3)')[0].text.strip()
    title_list.append(title_text)
    field_text = soup.select('#contents > div:nth-child(4) > ul > li:nth-child(1)')[0].text.strip()
    field_text = field_text.strip().split(': ', 1)[1] if field_text else 'N/A'
    field_list.append(field_text)
    content_text = soup.select('#contents > div:nth-child(4) > ul > li:nth-child(2)')[0].text.strip()
    content_text += '\n' + soup.select('#contents > div:nth-child(4) > ul > li:nth-child(3)')[0].text.strip()
    content_text += '\n' + soup.select('#contents > div:nth-child(4) > ul > li:nth-child(4)')[0].text.strip()
    content_list.append(content_text)
    way_list.append('전화 신청: 서초구보건소 건강관리과 모자보건팀 ☎ 02-2155-8067')
    etc_text = soup.select('#contents > div:nth-child(4) > ul > li:nth-child(5)')[0].text.strip()
    etc_text = etc_text.split(': ', 1)[1] if ': ' in etc_text else 'N/A'
    etc_list.append(etc_text)
    category_list.append(1) # 임신/출산
    host_list.append(1165000000) # 서초구 행정코드
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


# 임산부 건강관리
def extract_content(soup, header_idx, div_idx):
    # 제목 추출
    title_text = soup.select(f'#contents > h4:nth-child({header_idx})')[0].text.strip()

    # 필드 추출
    field_text = soup.select(f'#contents > div:nth-child({div_idx}) > ul > li:nth-child(1)')[0].text.strip()
    field_text = field_text.split(': ', 1)[1] if ': ' in field_text else 'N/A'

    # 내용 추출
    content_texts = []
    for i in range(2, 5):
        li_elements = soup.select(f'#contents > div:nth-child({div_idx}) > ul > li:nth-child({i})')
        if li_elements:
            li_text = li_elements[0].text.strip()
            # '문의' 또는 '신청'이 포함되지 않은 경우에만 추가
            if '문의' not in li_text and '신청' not in li_text:
                content_texts.append(li_text)
    content_text = '\n'.join(content_texts)

    # etc_text 추출 (li:nth-child(6)이 없을 경우 기본값 사용)
    etc_elements = soup.select(f'#contents > div:nth-child({div_idx}) > ul > li:nth-child(6)')
    if etc_elements:
        etc_text = etc_elements[0].text.strip()
        etc_text = etc_text.split(': ', 1)[1] if ': ' in etc_text else '서초모자보건지소 나를 찾는 방 02-2155-7586'
    else:
        etc_text = '서초모자보건지소 나를 찾는 방 02-2155-7586'

    return {
        'title': title_text,
        'field': field_text,
        'content': content_text,
        'etc': etc_text
    }

def sh1_page_crawler(url):
    # 데이터 초기화
    admin_list = []
    category_list = []
    host_list = []
    title_list = []
    field_list = []
    content_list = []
    url_list = []
    way_list = []
    etc_list = []

    # URL로부터 페이지 내용 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 공통 정보
    admin_id = 'teamwemmy@gmail.com'
    category_id = 1  # 임신/출산
    host_id = 1165000000  # 서초구 행정코드
    way = '- 건강부모e음 https://parents.seocho.go.kr/site/seochobogun/main.do 회원가입 후 건강부모교육에서 해당 강좌신청'

    # 임신부 건강관리
    title_list.append('임신부 건강관리')
    field_list.append('서초구 임산부')
    content_text = (
        '1. 엽산제 및 철분제 제공'
        '\n- 엽산제: 12주까지'
        '\n- 철분제: 16주~분만전까지 '
        '\n2. 임산부 검사'
        '\n- 모성검사: 평일 09시~11시, 13시~16시30분 가능'
        '\n- 검사명: 임신초기검사 / 시기: ~12주 / 검사내용: 풍진 항체검사, 혈액&소변검사(33종) / 검사시간: 평일(09시~11시, 13시~16시30분) / 결과지 수령일: 검사후 1주일 뒤 (인터넷 출력 가능)'
        '\n- 검사명: 기형아검사(전화예약필수) / 시기: 16~18주 / 검사내용: 채혈(퀴드검사_, 복부초음파(임신 주수 확인) / 결과지 수령일: 검사후 7일 뒤 (인터넷 출력 불가)'
        '\n- 검사명: 비타민D검사 / 시기: 16~20주 / 검사내용: 비타민D검사 후 수치에 따라 비타민D포함 종합영양제 지원 / 결과지 수령일: 검사후 5일 뒤 (인터넷 출력 가능)'
        '\n- 검사명: 임신성 당뇨검사,빈혈검사 / 시기: 24~28주 / 검사내용: 보건소에서 당뇨시약 마시고 1시간 후 채혈 (검사 전 금식 불필요) / 검사시간: 평일(09:00~10:30, 13:00~15:30) / 결과지 수령일: 검사후 1주일 뒤 (인터넷 출력 가능)'
        '\n- 검사명: 백일해예방접종 / 시기: 27~36주 / 검사내용: 벡일해예방접종(임신시마다 1회접종) / 접종비용: 무료'
        '\n- 결과지 인터넷 출력법: 보건소 홈페이지 → 우측 제증명 발급→인터넷 발급조회 → 검사결과온라인 조회 → 모성검사 결과 조회 → 사이트 이동(주민번호 입력, 공인인증서 본인 인증 절차 후) 조회 및 출력 가능'
    )
    content_list.append(content_text)
    way_list.append('- 보건소 방문\n평 일 : 09시~18시, 점심시간(12시~13시 제외)')
    etc_list.append(
        '- 서초구보건소 1층 모성실(02-2155-8065,8066,8067) 지하철 3호선, 신분당선 양재역 12번 출구\n'
        '- 방배보건지소 모성실(02-2155-8154,8155) 지하철 7호선 내방역 6번 출구(방배열린문화센터 2층)\n'
        '- 서초모자보건지소 건강클리닉(02-2155-8278) 지하철 2호선 서초역 4번 출구(마제스타시티 TOWER 2 건너편 1층)'
    )
    category_list.append(category_id)
    host_list.append(host_id)
    admin_list.append(admin_id)
    url_list.append(url)

    # 각 항목에 대해 반복적으로 데이터를 추출하여 추가
    header_div_pairs = [
        (7, 8), (9, 10), (11, 12), (13, 14), (15, 16),
        (17, 18), (19, 20), (21, 22), (23, 24), (25, 26),
        (27, 28), (29, 30)
    ]

    for header_idx, div_idx in header_div_pairs:
        extracted = extract_content(soup, header_idx, div_idx)
        title_list.append(extracted['title'])
        field_list.append(extracted['field'])
        content_list.append(extracted['content'])
        etc_list.append(extracted['etc'])
        category_list.append(category_id)
        host_list.append(host_id)
        admin_list.append(admin_id)
        url_list.append(url)
        way_list.append(way)

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
        'original_url': url_list
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id
    df.index = df.index + 1

    return df


# 각 크롤링한 내용 한번에 합쳐서 저장
def sh_crawler(urls):
    merged_df = pd.DataFrame()  # 모든 데이터프레임을 병합할 데이터프레임

    for url in urls:
        if url == url1:
            df = sh1_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url2:
            df = sh2_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url3:
            df = sh3_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url4:
            df = sh4_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print("지원하지 않는 URL입니다.")

    # CSV 파일 저장
    save_dir = '../[지역구]/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    csv_file_path = os.path.join(save_dir, f"서초구_{today}_검색결과.csv")
    merged_df.to_csv(csv_file_path, encoding='utf-8-sig', index=False)
    print('CSV 파일 저장 완료:', csv_file_path)

    # 데이터 프레임을 JSON 형식으로 변환하여 저장
    json_data = merged_df.to_json(orient='records', force_ascii=False)
    json_file_path = os.path.join(save_dir, f"sh_{today}_result.json")

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

# 서초구 검색 사이트
url1 = 'https://www.seocho.go.kr/site/sh/03/10304020100002020031909.jsp'
url2 = 'https://www.seocho.go.kr/site/sh/03/10304011100002020031805.jsp'
url3 = 'https://www.seocho.go.kr/site/sh/03/10304011200002020031805.jsp'
url4 = 'https://www.scscc.or.kr/care/index.asp'

# 여러 페이지 크롤링 및 저장
urls = [url1, url2, url3, url4]  # 크롤링할 페이지의 URL 리스트
sh_crawler(urls)




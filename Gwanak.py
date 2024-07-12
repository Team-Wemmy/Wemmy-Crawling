#  육아종합지원센터
def ga6_page_crawler(url):
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
    title_text = soup.select('#wrap > div.main-spot > div > dl > dt')[0].text.strip()
    title_list.append(title_text)
    field_list.append('관악구민(관악구 소재 직장인)으로 취학 전 아동이 있는 가정')
    content_list.append('어린이집 이용 아동·부모, 어린이집 보육 교직원·원장, 보육에 관심있는 일반인 등을 위해 보육에 관한 다양한 정보를 신속하고 체계적으로 제공')
    way_list.append('서울관악구육아종합지원센터 홈페이지 https://www.gwanak.go.kr/site/educare/main.do 회원가입')
    etc_list.append('서울관악구 육아종합지원센터 (02-851-2834)')
    category_list.append(2) # 영유아
    host_list.append(1162000000)  # 관악구 행정코드
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

#  서울형 가사서비스  페이지 크롤러 
def ga5_page_crawler(url):
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
    title_list.append('서울형 가사서비스 지원사업')
    field_list.append('관악구 거주 기준중위소득 150%이하 임산부, 맞벌이, 다자녀 가구'+'\n'+'- 임산부 가구 : 임신~출산 후 1년 이내 가구'+'\n'+'- 맞벌이 가구 : 부부 모두 주 20시간 이상 근로하고 있는 가구'+'\n'+'- 다자녀 가구 : 미성년 자녀(만18세이하)가 2명 이상인 가구')
    content_list.append('- 내용: 거주지 가사서비스 지원(방/ 거실/ 주방/ 화장실 청소, 설거지, 쓰레기 배출, 세탁 등)'+'\n'+'※ 제외업무 : 정리정돈, 취사, 아이돌봄, 반려동물 돌봄, 입주청소, 전문자격 요하는 서비스 등'+'\n'+'- 지원횟수: 1가구당 총 10회(1회당 4시간, 30분 휴게시간 포함)'+'\n'+'- 이용요금: 본인부담금 없음'+ '\n'+'- 신청기간: 2024. 2월말(예정) ~ 11. 30.')
    way_list.append('- 온라인: 서울가족포털 온라인 신청(www.familyseoul.or.kr)')
    etc_list.append('여성가족과 (02-879-6133)')
    category_list.append(1) # 임신/출산
    host_list.append(1162000000)  # 관악구 행정코드
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

#  엄빠택시 페이지 크롤러
def ga4_page_crawler(url):
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
    title_list.append('서울엄마아빠택시 시범사업')
    field_list.append('관악구 거주 영아(24개월 이하) 양육가정')
    content_list.append('- 내용: 영아용 카시트가 구비된 택시 이용권 영아 1인당 연 10만원 지원'+'\n'+'- 사용용도: 양육자가 영아 동반 외출 시 이동 목적 제한 없이 사용'+'\n'+'- 신청기간: 2024. 1. 23.(화) ~ 11. 30.(토)'+'\n'+'- 이용기간: 2024. 12. 15.(일)까지')
    way_list.append('- 서비스 운영사(아이엠.택시, i.M) 모바일 앱 설치, 구비서류 등록 후 신청'+'\n'+'구비서류 : 영아와 함께 등재된 주민등록등본(주민등록번호 뒷자리 제외) 업로드')
    etc_list.append('여성가족과 (02-879-6133)')
    category_list.append(2) # 영유아
    host_list.append(1162000000)  # 관악구 행정코드
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

#  유축기 대여
def ga3_page_crawler(url):
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
    title_list.append('유축기 대여')
    field_list.append('출산 6개월 이내 관악구 산모')
    content_list.append('대여기간 : 1개월'+'\n'+'준비물 : 산모신분증, 예약문자'+'\n'+'※가족 대리 방문가능 (준비물 + 대리인 신분증), 보건소 미등록 산모는 출생증명서 추가필요'+'\n'+'유축기 제품명 : 스펙트라 전동식 모유착유기 (깔대기 포함)')
    way_list.append('- 대여방법 : 온라인 신청 후 방문하여 수령'+'\n'+'- 보건소 홈페이지 -> 온라인 서비스 -> 인터넷 예약 클릭하여 원하는 대여일자 신청 -> 예약문자 확인 -> 예약일 후 3일 내에 방문 수령'+'\n'+'- 보건소 방문시간: 09:00~11:30, 13:00~17:30')
    etc_list.append('보건소 5층 모성실 (02-879-7156)')
    category_list.append(1) # 임신/출산
    host_list.append(1162000000)  # 관악구 행정코드
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


# 모유수유 안내
def extract_info2(soup, h4_indices, ul_indices, li_indices, way_index=None):
    # 제목 추출
    title_text = soup.select(f'#contents > h4:nth-child({h4_indices[0]})')[0].text.strip()
    
    # 지원대상 추출
    field_element = soup.select(f'#contents > ul:nth-child({ul_indices[0]}) > li:nth-child({li_indices[0]})')
    field_text = field_element[0].text.strip().split(': ', 1)[1] if field_element else 'N/A'
    
    # 내용 추출
    content_text = []
    for li_index in li_indices:
        content_elements = soup.select(f'#contents > ul:nth-child({ul_indices[0]}) > li:nth-child({li_index})')
        content_text.extend([el.text.strip() for el in content_elements])
    
    # 추가 내용 추출
    additional_content_elements = soup.select(f'#contents > ul:nth-child({ul_indices[1]}) > li')
    additional_content_text = '\n'.join(el.text.strip() for el in additional_content_elements)
    
    # 내용 통합
    full_content_text = '\n'.join(content_text) + '\n' + additional_content_text
    
    # 신청 방법 추출
    way_text = soup.select(f'#contents > ul:nth-child({ul_indices[0]}) > li:nth-child({way_index})')[0].text.strip() if way_index else 'N/A'
    
    # 문의처 추출
    etc_element = soup.select(f'#contents > h4:nth-child({h4_indices[2]})')
    etc_text = etc_element[0].text.strip().split(': ', 1)[1] if etc_element else 'N/A'
    
    return title_text, field_text, full_content_text, way_text, etc_text

def ga2_page_crawler(url):
    # 정보 담을 리스트 초기화
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

    # 데이터 추출
    title_text, field_text, content_text, way_text, etc_text = extract_info2(
        soup,
        h4_indices=[1, 3, 5],
        ul_indices=[2, 4],
        li_indices=[1, 2, 3, 4, 7],
        way_index=6
    )

    # 리스트에 추가
    title_list.append(title_text)
    field_list.append(field_text)
    content_list.append(content_text)
    way_list.append(way_text)
    etc_list.append(etc_text)
    category_list.append(1)  # 임신/출산
    host_list.append(1162000000)  # 관악구 행정코드
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
        'original_url': url_list
    })

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df


# 임산부 등록관리
def extract_info1(soup, h4_index, ul_index, li_indices, way_index=None):
    title_text = soup.select(f'#contents > h4:nth-child({h4_index})')[0].text.strip()
    field_text = soup.select(f'#contents > ul:nth-child({ul_index}) > li:nth-child({li_indices[0]})')[0].text.strip()
    field_text = field_text.split(': ', 1)[1] if ': ' in field_text else 'N/A'
    
    content_text = '\n'.join(soup.select(f'#contents > ul:nth-child({ul_index}) > li:nth-child({i})')[0].text.strip() for i in li_indices[1:])
    
    way_text = '방문: 보건소 5층 모성실' + '\n'
    if way_index is not None:
        way_text += soup.select(f'#contents > ul:nth-child({ul_index}) > li:nth-child({way_index})')[0].text.strip()
    if '온라인' not in way_text:
        way_text += '\n온라인: 정부24 맘편한임신 (https://www.gov.kr/portal/onestopSvc/fertility)'
    
    etc_text = soup.select('#contents > ul:nth-child(18) > li:nth-child(1)')[0].text.strip()
    
    return title_text, field_text, content_text, way_text, etc_text

def ga1_page_crawler(url):
    # 정보 담을 리스트 초기화
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

    # 데이터 추출
    def process_section(h4_index, ul_index, li_indices, way_index=None):
        title_text, field_text, content_text, way_text, etc_text = extract_info1(soup, h4_index, ul_index, li_indices, way_index)
        title_list.append(title_text)
        field_list.append(field_text)
        content_list.append(content_text)
        way_list.append(way_text)
        etc_list.append(etc_text)
        category_list.append(1)  # 임신/출산
        host_list.append(1162000000)  # 관악구 행정코드
        admin_list.append('teamwemmy@gmail.com')
        url_list.append(url)
    
    # 추가 임신초기검사
    process_section(5, 6, [1, 2, 3, 4, 5])

    # 추가 산전기형아선별검사
    process_section(7, 8, [1, 2, 3, 4, 5, 6], way_index=7)

    # 추가 엽산제 지원
    process_section(9, 10, [1, 2, 3])

    # 추가 철분제 지원
    process_section(11, 12, [1, 2, 3])

    # 추가 임산부 체험복 대여
    process_section(15, 16, [1, 2, 3, 5])

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

    # 각 페이지에 대해 유니크한 아이디 생성 및 추가 (10자리 숫자로 변환)
    unique_id = [(int(uuid.uuid4().int) % 10000000000) for _ in range(len(df))]
    df['unique_id'] = unique_id

    df.index = df.index + 1

    return df

# 각 크롤링한 내용 한번에 합쳐서 저장
def ga_crawler(urls):
    merged_df = pd.DataFrame()  # 모든 데이터프레임을 병합할 데이터프레임

    for url in urls:
        if url == url1:
            df = ga1_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url2:
            df = ga2_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url3:
            df = ga3_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url4:
            df = ga4_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url5:
            df = ga5_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url6:
            df = ga6_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print("지원하지 않는 URL입니다.")

    # CSV 파일 저장
    save_dir = '../[지역구]/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    csv_file_path = os.path.join(save_dir, f"관악구_{today}_검색결과.csv")
    merged_df.to_csv(csv_file_path, encoding='utf-8-sig', index=False)
    print('CSV 파일 저장 완료:', csv_file_path)

    # 데이터 프레임을 JSON 형식으로 변환하여 저장
    json_data = merged_df.to_json(orient='records', force_ascii=False)
    json_file_path = os.path.join(save_dir, f"ga_{today}_result.json")

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

# 관악구 검색 사이트
url1 = 'https://www.gwanak.go.kr/site/health/04/10402010000002016051301.jsp'
url2 = 'https://www.gwanak.go.kr/site/health/05/10502050700002023020305.jsp'
url3 = 'https://www.gwanak.go.kr/site/health/05/10502050300002022080207.jsp'
url4 = 'https://www.gwanak.go.kr/site/gwanak/04/10407020100002016051205.jsp'
url5 = 'https://www.gwanak.go.kr/site/gwanak/06/10614020400002024022010.jsp'
url6 = 'https://www.gwanak.go.kr/site/educare/main.do'

# 여러 페이지 크롤링 및 저장
urls = [url1, url2, url3, url4, url5, url6]  # 크롤링할 페이지의 URL 리스트
ga_crawler(urls)
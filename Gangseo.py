# 강서육아종합 페이지 크롤러
def gs4_page_crawler(url):
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

    # 추가
    title_list.append('서울강서구육아종합지원센터')
    field_list.append('강서구민(강서구 소재 직장인)으로 취학 전 아동이 있는 가정')
    content_list.append('강서구내 영유아와 부모, 어린이집, 보육교직원들을 대상으로 전문적인 보육서비스를 제공하고, 보육네트워크를 통한 보육정책을 실현')
    way_list.append('서울강서구육아종합지원센터 홈페이지 https://www.gskids.or.kr/ 회원가입')
    etc_list.append('서울강서구 육아종합지원센터 (02-2064-0119)')
    category_list.append(2) # 영유아
    host_list.append(1150000000) # 강서구 행정코드
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


# 유축기 대여 페이지 크롤러
def gs3_page_crawler(url):
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

    # 추가
    title_list.append('전동 유축기 대여')
    field_list.append('관내 모유수유를 원하는 산모')
    content_list.append('- 유축기 대여 예약 접수 후 2개월 간 대여'+'\n'+'- 기간 : 연 중(토요일 대여 불가), 점심시간: 12시 ~ 13시' +'\n'+'- 준비물 : 주민등록등본(3개월이내 발급), 산모신분증 (대리인 수령 시 대리인 신분증도 지참)※ 접속일로부터 3일 뒤부터 수령일 지정가능. 병원 및 조리원 퇴소 최소 3일전에 신청요망')
    way_list.append('보건소 홈페이지 유축기 대여 예약 접수 (https://www.gangseo.seoul.kr/health/ht050202)')
    etc_list.append('보건소 1층 모성실(02-2600-5895/5917)')
    category_list.append(1) # 임신/출산
    host_list.append(1150000000) # 강서구 행정코드
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

# 행복수유 페이지 크롤러
def gs2_page_crawler(url):
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

     # 추가
    title_list.append('서울맘 찾아가는 행복수유 지원')
    field_list.append('출산 후 8주 이내 모유수유를 희망하는 관내 임산부 (신청일 기준, 주민등록상 6개월 이상 서울시 거주)')
    content_list.append('◦ 지원시기: 예산 소진시까지'+'\n'+'- 제출서류: 신청서, 개인정보 수집 및 이용 동의서, 주민등록등본 (※ 주민등록등본 과거의 주소 변동사항 최근 1년 포함)' +'\n'+'◦ 지원: 임산부 자택 방문 모유수유 관리 1시간'+'\n'+'- 임산부 유방상태 진단에 따른 맞춤형 유방마사지'+'\n'+'- 모유수유 방법(자세, 유방관리 등) 교육'+'\n'+'- 신생아 모유수유 직접 시도 및 평가 지도'+'\n'+'- 임산부 가족대상 모유수유 지지 교육 및 상담(가족 참여시)'+'\n'+'◦ 지원횟수: 1인당 최대 2회(무료)'+'\n'+'◦ 서비스 제공인력: 강서구 선정 모유수유 매니저'+'\n'+'- 모유수유 매니저란? 서울시와 업무협약한 의료인 단체가 운영하는「모유수유 전문가 과정」을 이수한 간호사(조산사)'+'\n'+'◦ 서비스 제공 장소: 임산부가 지정하는 주택(강서구 소재지)')
    way_list.append('서울시임신출산정보센터(https://seoul-agi.seoul.go.kr)')
    etc_list.append('보건소 1층 모성실(02-2600-5895/5917)')
    category_list.append(1) # 임신/출산
    host_list.append(1150000000) # 강서구 행정코드
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


#  임산부 등록  페이지 크롤러
def gs1_page_crawler(url):
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

     # 추가
    title_list.append('임산부 등록관리')
    field_list.append('관내 임산부')
    content_text = '◦ 시기: 연중' +'\n' + '- 평일: 월~금 09:00~18:00' + '\n' +'- 강서구 슬기로운 보건소 운영 : 2023년 5월 ~12월 (공휴일 제외) 매달 둘째주 토요일 09:00~13:00'
    content_text += '\n' + '◦ 준비물' +'\n' + '- 기본 : 산모 신분증, 출산예정일이 기재된 임신확인서 또는 산모수첩' +'\n' + '- 모성실 검사 및 유축기 대여 : 산모 등본(3개월 이내)' + '\n' +'- 유축기 대리수령 시 : 산모 등본(3개월 이내), 대리인 신분증' + '\n' +'- 영양제 대리수령 시 : 산모와 대리인 함께 등재된 등본(3개월 이내) 또는 가족관계증명서, 대리인 신분증'
    content_text += '\n' + '◦ 제공내용' +'\n' + '- 임산부 등록 / 시기: 임신확인시 / 산부인과에서 힘식 확진 받은 이후 등록 / 온라인 또는 방문' + '\n' + '- 임신초기검사 / 시기: 임신10주 이내 / 풍진검사, 빈혈(CBC), 매독·AIDS검사, 혈액형, 혈당, 간기능, B형간염 (※ 8시간 이상 금식 평일 9시~11시 / 13시~17시) / 방문'+ '\n' + '- 혈압·체중 / 시기: 방문시 / 혈압 및 체중 측정 / 방문'+ '\n' + '- 태아 혈청 기형아 검사 / 시기: 임신 16주~18주 / 2차기형아검사(퀴드)(※ 금식 필요 없음, 평일 9시~11시 / 13시~17시) / 방문'+'\n'+'- 엽산제지원 / 시기: 임신 16주까지 / 임신주수에 맞춰 최대 3개월분 지원 / 온라인 또는 방문' + '\n'+ '- 철분제지원 / 시기: 임신 16주~분만전 / 임신 잔여기간에 한해 최대 5개월분 지원 (※ 등록된 임산부에 한하여 배우자 및 직계존속 대리수령 가능, 대리수령시 구비서류: 산모신분증, 대리인신분증, 주민등록등본(가족관계증명서)) / 온라인 또는 방문' + '\n' + '- 임신성당뇨검사 / 시기: 임신 24주~28주 / 식사후 물포함 3시간 금식 후 내소 -> 글루오렌지시약 섭취 -> 1시간 후 검사 (※ 평일 9시~10시30분/ 13시~16시) / 방문'
    content_text += '\n' + '※ 온라인으로 택배(엽산제, 철분제, 모자보건수첩, 임산부표시 배지 지원) 신청시 택배비 본인부담'
    content_list.append(content_text)
    way_list.append('- 온라인: 정부24(https://www.gov.kr/portal/main) → 원스톱 서비스 → 맘편한임신 또는 임신육아종합포털 아이사랑 (e보건소연계)'+'- 방 문: 보건소 1층 모성실')
    etc_list.append('보건소 1층 모성실(02-2600-5895/5917)')
    category_list.append(1) # 임신/출산
    host_list.append(1150000000) # 강서구 행정코드
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
def gs_crawler(urls):
    merged_df = pd.DataFrame()  # 모든 데이터프레임을 병합할 데이터프레임

    for url in urls:
        if url == url1:
            df = gs1_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url2:
            df = gs2_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url3:
            df = gs3_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif url == url4:
            df = gs4_page_crawler(url)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print("지원하지 않는 URL입니다.")

    # CSV 파일 저장
    save_dir = '../[지역구]/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    csv_file_path = os.path.join(save_dir, f"강서구_{today}_검색결과.csv")
    merged_df.to_csv(csv_file_path, encoding='utf-8-sig', index=False)
    print('CSV 파일 저장 완료:', csv_file_path)

    # 데이터 프레임을 JSON 형식으로 변환하여 저장
    json_data = merged_df.to_json(orient='records', force_ascii=False)
    json_file_path = os.path.join(save_dir, f"gs_{today}_result.json")

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

# 강서구 검색 사이트
url1 = 'https://www.gangseo.seoul.kr/health/ht020213'
url2 = 'https://www.gangseo.seoul.kr/health/ht020220'
url3 = 'https://www.gangseo.seoul.kr/health/ht020215'
url4 = 'https://www.gskids.or.kr/'

# 여러 페이지 크롤링 및 저장
urls = [url1, url2, url3, url4]  # 크롤링할 페이지의 URL 리스트
gs_crawler(urls)

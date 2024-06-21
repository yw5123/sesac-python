from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import cine_database as my_db

import pandas as pd

import time

# 크롬 실행 시 필요한 옵션 추가
chrome_options = Options()
# chrome_options.add_argument("--headless")   # 브라우저를 숨겨서 실행
# chrome_options.add_argument("--window-size=1920,1000")

# 크롬 드라이버 서비스 생성
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 페이지 대기를 위한 웨이터 생성
# 안 나올 수도 있으니 기다리는 최대 시간을 줌 (최대 10초까지 기다려라..)
wait = WebDriverWait(driver, 10)

# 웹페이지 열기
base_url = 'http://www.cine21.com'
ranking_url = base_url + '/rank/boxoffice/domestic'
driver.get(ranking_url)


# 영화 목록 담기 위한 빈 변수
data = []

def get_movie_list():
    # 페이지 소스 가져오기
    page_source = driver.page_source

    # BS4로 전달해서 파싱
    # soup = BeautifulSoup(page_source, 'html.parser')
    # boxoffice_list_content = soup.find('div', id='boxoffice_list_content')
    # print(boxoffice_list_content)
    boxoffice_list_content = driver.find_element(By.ID, 'boxoffice_list_content')

    # 영화 순위, 영화 제목, 관객 수 출력하기
    movie_list = boxoffice_list_content.find_elements(By.CSS_SELECTOR, 'li.boxoffice_li')
    for movie in movie_list:
        mov_name_div = movie.find_element(By.CSS_SELECTOR, 'div.mov_name')
        people_num_div = movie.find_element(By.CSS_SELECTOR, 'div.people_num')
        grade_num_span = movie.find_element(By.CSS_SELECTOR, 'span.grade')

        a_link = movie.find_element(By.TAG_NAME, 'a')
        mov_link = a_link.get_attribute('href')

        rank = grade_num_span.text.strip()
        mov_name = mov_name_div.text.strip()
        people_num = people_num_div.text.strip().replace('관객수|','')

        # print(f'순위: {rank}, 영화 제목: {mov_name}, 관객수: {people_num}')
        # data.append({'순위': rank, '영화제목': mov_name, '관객수': people_num, '웹사이트정보': mov_link})
        my_db.save_to_db(conn, cur, rank, mov_name, people_num, mov_link)


# 두번째 페이지 가져오기
# page_tags = driver.find_elements(By.CSS_SELECTOR, "div.page a")
# print(page_tags)
# page_tags[1].click()

# 미션. 모든 페이지 영화 목록 다 가져오기
# 1. 2페이지로 이동
# 2. 2페이지의 내용 출력
# 3. 어?? 복붙했네.. 함수를 만든다
# 4. 함수에 페이지 번호를 인자값으로 준다?? <- 코딩하면서 함수 형태는 원하는대로
# 5. 1~10페이지까지 모든 내용

# time.sleep(5)


conn, cur = my_db.init_db()

for page in range(0,10):
    # 페이지 목록 div가 뜰 때까지 기다린다.
    # page_tags = driver.find_elements(By.CSS_SELECTOR, "div.page a")
    page_tags = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.page a')))
    page_tags[page].click()
    # 혹시 모르니 클릭한 후에 내가 원하는 내용이 떴는지 확인
    # wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#boxoffice_list_content li.boxoffice_li')))    # 이미 있어서 작동하지 않음
    time.sleep(2)

    get_movie_list()

# print(data)

# 미션2. 가져온 내용 DB에 넣기
# 1. DB 테이블 생성 (스키마 설계)
# 2. 리스트에 있는 내용을 DB에 삽입 (SQL 쿼리문)

my_db.query_movie(cur)

my_db.close_db(conn)

    

# 브라우저 닫기
driver.quit()
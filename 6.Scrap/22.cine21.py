from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import pandas as pd

import time

# 크롬 실행 시 필요한 옵션 추가
chrome_options = Options()
# chrome_options.add_argument("--headless")   # 브라우저를 숨겨서 실행
# chrome_options.add_argument("--window-size=1920,1000")

# 크롬 드라이버 서비스 생성

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 웹페이지 열기
base_url = 'http://www.cine21.com'
ranking_url = base_url + '/rank/boxoffice/domestic'
driver.get(ranking_url)

# 페이지 소스 가져오기
page_source = driver.page_source

# BS4로 전달해서 파싱
soup = BeautifulSoup(page_source, 'html.parser')
boxoffice_list_content = soup.find('div', id='boxoffice_list_content')
# print(boxoffice_list_content)

# 영화 목록 담기 위한 빈 변수
data = []

# 영화 순위, 영화 제목, 관객 수 출력하기
movie_list = boxoffice_list_content.select('.boxoffice_li')
for movie in movie_list:
    mov_name_div = movie.find('div', class_='mov_name')
    people_num_div = movie.find('div', class_='people_num')
    grade_num_span = movie.find('span', class_="grade num1")

    mov_link = base_url + movie.find('a')['href']

    rank = grade_num_span.get_text(strip=True)
    mov_name = mov_name_div.get_text(strip=True)
    people_num = people_num_div.get_text(strip=True).replace('관객수|','')

    # print(f'순위: {rank}, 영화 제목: {mov_name}, 관객수: {people_num}')
    data.append({'순위': rank, '영화제목': mov_name, '관객수': people_num, '웹사이트정보': mov_link})

# time.sleep(5)
# print(data)

df = pd.DataFrame(data)
# 엑셀로 저장
df.to_excel('boxoffice_rankings.xlsx')

# 브라우저 닫기
driver.quit()
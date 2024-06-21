# pip install selenium

# 나중에 크롬 드라이버 버전이 안맞으면 문제 발생..
# 크롬 드라이버를 관리해주는 드라이버 라이브러리가 있음..
# pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

# 크롬 실행 시 필요한 옵션 추가
chrome_options = Options()
chrome_options.add_argument("--headless")   # 브라우저를 숨겨서 실행
chrome_options.add_argument("--window-size=1920,1000")

# 크롬 드라이버 서비스 생성
# service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 웹페이지 열기
driver.get('https://www.google.com')

# 검색창에 원하는 글자 입력
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("Python Programming")

# 엔터를 치던지 검색 버튼을 가져와서 클릭을 하던지
# search_box.submit()
search_box.send_keys(Keys.RETURN)

time.sleep(5)

# 결과 페이지 스크린샷
driver.save_screenshot('search_result_003.png')

# 브라우저 닫기
driver.quit()
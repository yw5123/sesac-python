# pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 크롬 드라이버 서비스 생성
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 웹페이지 열기
driver.get('https://www.naver.com')

# 브라우저 닫기
driver.quit()
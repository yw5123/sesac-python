import requests
from bs4 import BeautifulSoup

url = 'https://sports.news.naver.com/index'

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

# 신문 기사 제목 및 링크 출력하기

# today_ul = soup.find('ul', class_='today_list')

# today_lis = today_ul.select('.today_item')

# for today_li in today_lis:
#     today_a = today_li.find('a')
#     print(f"기사 제목: {today_a['title']}")
#     print(f"기사 링크: {today_a['href']}")
#     print()


news_list = soup.select('.today_list > li')

for news in news_list:
    a_tag = news.select_one('a')
    print(a_tag['title'])
    print(a_tag['href'])
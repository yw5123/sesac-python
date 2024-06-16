import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/section/105'

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

print("-" * 10 + " 헤드라인 뉴스 " + "-" * 10)

head_li = soup.select('.as_section_headline > .section_article > ul > li')

for headnews in head_li:
    news = headnews.select_one('.sa_item_inner > .sa_item_flex > .sa_text > a')
    strong = news.find('strong')
    print("기사 제목: " + strong.get_text())
    print("기사 링크: " + news['href'])
    print()

print("-" * 10 + " 일반 뉴스 " + "-" * 10)

news_div = soup.select('.section_latest_article > .section_article')

for div in news_div:
    news_li = div.select('.sa_list > li')
    for li in news_li:
        news = li.select_one('.sa_item_inner > .sa_item_flex > .sa_text > a')
        strong = news.find('strong')
        print("기사 제목: " + strong.get_text())
        print("기사 링크: " + news['href'])
        print()
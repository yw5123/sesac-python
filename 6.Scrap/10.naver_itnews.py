import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/section/105'

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

def print_articles(section_articles):
    for section_article in section_articles:
        sa_text_titles = section_article.find_all('a', class_='sa_text_title')
        for sa_text_title in sa_text_titles:
            print(sa_text_title.get_text().strip())

# 신문 기사제목 및 링크 출력
# 헤드라인 출력

# 헤드라인 섹션 가져오기
# section_articles = soup.find_all('div', class_="section_article as_headline _TEMPLATE")
section_articles = soup.select("div.section_article.as_headline._TEMPLATE")

print_articles(section_articles)

print('-' * 50)

section_articles = soup.select('div.section_article._TEMPLATE')
print_articles(section_articles)


## ----------------------------
# 이렇게도 가능

def print_articles(headline=True):
    if headline:
        section_articles = soup.select("div.section_article.as_headline._TEMPLATE")
    else:
        section_articles = soup.select('div.section_article._TEMPLATE')

    for section_article in section_articles:
        sa_text_titles = section_article.find_all('a', class_='sa_text_title')
        for sa_text_title in sa_text_titles:
            print(sa_text_title.get_text().strip())

print_articles(True)
print('-' * 50)
print_articles(False)
# pip install bs4

from bs4 import BeautifulSoup

html_doc="""
<html>
<head>
    <title>간단한 html 예제</title>
</head>
<body>
    <div class="container">
        <h1>안녕하세요</h1>
        <p>이것은 간단한 html 예제</p>
    </div>
    <a href="https://www.naver.com">네이버 링크</a>
    <img src="example.jpg" alt="예제 이미지">
    <img src="example2.jpg" alt="예제 이미지2" width="500" height="600">
    <div class="content">
        <ul>
            <li>항목 1</li>
            <li>항목 2</li>
            <li>항목 3</li>
        </ul>
    </div>
    <div id="footer">
        <p>Copyright ⓒ 2024. 이 페이지 내꺼</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, lxml.parser

list_items = soup.ul.find_all('li')
# print(list_items)

# for li in list_items:
#     print(li.text)

# print(list_items[1].text)

# 클래스가 container인 항목 가져오기
container_div = soup.find('div', class_='container')    # class만 예약어라 밑줄이 붙음
# print(container_div.h1.text)
# print(container_div.p.text)

# footer를 가져다가 그 안에 있는 글자 출력하기
footer_div = soup.find('div', id="footer")
# print(footer_div.p.text)

# content_ul = soup.find('div', class_="content").ul
# print(content_ul)

# for li in content_ul.find_all('li'):
#     print(li.text)

link_tag = soup.a   # 가장 먼저 DOM에서 잡히는 a 태그
# print(link_tag.text)
# naver_link = link_tag['href']
# print(link_tag['href'])

# import requests
# response = requests.get(naver_link)
# print(response.text)
# 네이버 링크의 데이터 가져옴. 이런식으로 계속 반복 가능

img_tag = soup.img
print(img_tag['src'])
print(img_tag['alt'])

img_tags = soup.find_all('img')
img_tag1 = img_tags[0]
img_tag2 = img_tags[1]
print(f'이미지 태그1: ', img_tag1)
print(f'이미지 태그2: ', img_tag2)

print(f"소스: {img_tag.get('src')}, ALT 글자: {img_tag.get('alt')}, Width: {img_tag.get('width', '없음')}")
print(f"소스: {img_tag2.get('src')}, ALT 글자: {img_tag2.get('alt')}, Width: {img_tag2.get('width', '없음')}")


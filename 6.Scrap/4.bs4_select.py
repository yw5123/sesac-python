# pip install bs4

from bs4 import BeautifulSoup

# import requests
# html_doc = requests.get('https://www.naver.com').text
# 이런식으로 정보를 가져왔다고 치고 간단한 html로 실습

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
        <p>Copyright ⓒ <b>2024.</b> 이 <i>페이지</i> 내꺼</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, lxml.parser

link_tag = soup.select_one('a')
print(link_tag)

all_imgs = soup.select('img')
print(all_imgs)
for img in all_imgs:
    print(img['src'])

content_div = soup.select_one('div.content')    # div 아래 있는 .content (클래스명)
print(content_div)

footer_div = soup.select_one('div#footer')  # ID로 갖고 오고 싶다면..
print(footer_div)

li_lists = soup.select('div.content li')    # div 아래 있는 content 클래스 아래 있는 li들
print(li_lists)

# li_lists = soup.find_All('div.content li')    # 이렇게는 안 됨.. find는 태그명 등으로 검색

p_tag_div_footer = soup.select_one('div#footer p')
b_text = p_tag_div_footer.select_one('b').get_text()
i_text = p_tag_div_footer.select_one('i').get_text()

print(f"볼드 텍스트: {b_text}, 이탤릭 텍스트: {i_text}")
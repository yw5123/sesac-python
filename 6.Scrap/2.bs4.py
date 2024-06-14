# pip install bs4

from bs4 import BeautifulSoup

html_doc="""
<html>
<head>
    <title>간단한 html 예제</title>
</head>
<body>
    <h1>안녕하세요</h1>
    <p>이것은 간단한 html 예제</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, lxml.parser
# print(html_doc)
# print(soup)

print(soup.head)
print(soup.body.h1.text)
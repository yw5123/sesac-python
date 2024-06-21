import requests
from bs4 import BeautifulSoup

url = 'http://www.cine21.com/rank/boxoffice/domestic'
response = requests.get(url)

soup =BeautifulSoup(response.text, 'html.parser')
# print(soup)

boxoffice_list_content = soup.find('div', id='boxoffice_list_content')
print(boxoffice_list_content)
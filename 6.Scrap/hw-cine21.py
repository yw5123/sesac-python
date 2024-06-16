import requests
from bs4 import BeautifulSoup

url = 'http://www.cine21.com/rank/boxoffice/domestic'

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

movie_list = soup.select('#boxoffice_list_content')
print(movie_list)

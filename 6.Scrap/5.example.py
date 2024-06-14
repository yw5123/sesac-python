import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonscraping.com/pages/page3.html'

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

# 상품명과 가격 출력
# 웹브라우저에서 f12 들어가서 소스 보면서 원하는 정보가 어디있는지 확인

# 내가 작성하던 코드 - 안됐는데 아래 코드 완성 후 수정
# item_lists = soup.select('.gift')
# for item in item_lists:
#     item_info = item.select('td')
#     print(f"상품명: {item_info[0].get_text().strip()}, 가격: {item_info[2].get_text().strip()}")

# print("-" * 15)

# 실습 코드
# table_tag = soup.find('table', id="giftList") # 가져오는 방법은 여러가지
table_tag = soup.select_one('#giftList')

# product_trs = table_tag.find_all('tr')
product_trs = table_tag.select('.gift')

item_list = []

for product_tr in product_trs:
    product_tds = product_tr.select('td')
    # print(f"상품명: {product_tds[0].text.strip()}, 가격: {product_tds[2].text.strip()}")
    item_list.append((product_tds[0].text.strip(), product_tds[2].text.strip()))    # DB를 만든다면

for item in item_list:
    print(f"상품명: {item[0]}, 가격: {item[1]}")
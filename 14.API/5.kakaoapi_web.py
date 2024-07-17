# https://dapi.kakao.com/v2/search/web


# 이름	설명	필수
# Authorization	Authorization: KakaoAK ${REST_API_KEY}
# 인증 방식, 서비스 앱에서 REST API 키로 인증 요청	O

# query	String	검색을 원하는 질의어	O
# sort	String	결과 문서 정렬 방식, accuracy(정확도순) 또는 recency(최신순), 기본 값 accuracy	X
# page	Integer	결과 페이지 번호, 1~50 사이의 값, 기본 값 1	X
# size	Integer	한 페이지에 보여질 문서 수, 1~50 사이의 값, 기본 값 10	X


import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('KAKAO_API_KEY')

query = '이효리'

url = 'https://dapi.kakao.com/v2/search/web'
headers = {
    "Authorization": f"KakaoAK {API_KEY}"
}
params = {
    "query": query,
    "sort": "accuracy",    # 정확도순
    "page": 1,
    "size": 10
}

response = requests.get(url, headers=headers, params=params)
response.raise_for_status()
data = response.json()
for item in data["documents"]:
    title = item["title"].replace("<b>","").replace("</b>","")
    url = item["url"]
    print(f"제목 : {title}")
    print(f"URL : {url}")
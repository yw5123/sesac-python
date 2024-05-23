# pip install requests
import requests

# 리퀘스트 모듈 안의 함수 사용 가능

# 1. 웹페이지에 있는 컨텐츠 가져올 수 있음
# response = requests.get("https://www.example.com")
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("웹페이지 내용: ")
print(response)
print(response.status_code)
# print(response.text)

# text 결과물 가져온 것을 json 이란 데이터타입으로 변환
data = response.json()
# print("JSON 데이터: ", data)
# userId = data['userId']
# title = data['title']
# print(f'사용자ID: {userId}, 타이틀: {title}')

users = data
for user in users:
    print("이름: {}, ID: {}, 이메일: {}".format(user['name'], user['username'], user['email']))
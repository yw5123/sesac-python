# pip install python-dotenv # 이전에 install했음

import requests
from dotenv import load_dotenv
import os

# 파일을 읽어 메모리를 로딩
load_dotenv()
OWM_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Seoul',       # 버전 업그레이드되면서 hidden api가 되었음
    'appid': OWM_API_KEY,      # 키 파일은 절대절대절대 소스코드에 포함하지 않음
    'units': 'metric',  # 온도가 섭씨로 바뀜
    'lang': 'kr',       # 결과 언어 선택
}

response = requests.get(url, params=params)
response.raise_for_status()

weather_data = response.json()
city_name = weather_data['name']
temperature = weather_data['main']['temp']
description = weather_data['weather'][0]['description']

print(f'도시: {city_name}')
print(f'온도: {temperature}')
print(f'날씨: {description}')
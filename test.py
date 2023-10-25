import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.worldfootball.net/schedule/eng-premier-league-2023-2024-spieltag/10/'

# URL에 GET 요청을 보내서 웹 페이지의 소스를 가져옴
response = requests.get(url)

# 응답 상태 코드 확인 (200은 성공을 나타냄)
if response.status_code == 200:
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = bs(response.text, 'html.parser')
    games = soup.find(class_='standard_tabelle').select("tr")
    # for i in soup.find(class_='standard_tabelle').select("tr")[0].find_all(class_='hell'):
    #     print(i)
    #     print()
    for i in games[2].find_all(class_='hell'):
        print(i.text)
        print()
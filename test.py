import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.worldfootball.net/schedule/eng-premier-league-2023-2024-spieltag/10/'

# URL에 GET 요청을 보내서 웹 페이지의 소스를 가져옴
response = requests.get(url)

# 응답 상태 코드 확인 (200은 성공을 나타냄)
if response.status_code == 200:
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = bs(response.text, 'html.parser')
    info = soup.find_all(class_='standard_tabelle')
    matches = info[0].select("tr")
    ranks = info[1].select("tr")
    
    rank_info = []
    for rank in ranks[1:]:
        rank_tmp = rank.select('td')
        tmp = [rank_tmp[0].text,
                rank_tmp[1].find('img').get('src'),
                rank_tmp[2].text,
                rank_tmp[3].text,
                rank_tmp[4].text,
                rank_tmp[5].text,
                rank_tmp[6].text,
                rank_tmp[7].text,
                ]
        rank_info.append(tmp)
    print(len(rank_info))
        # ranking = rank_tmp[0].text
        # logo = rank_tmp[1].find('img').get('src')
        # team_name = rank_tmp[2].text
        # match_num = rank_tmp[3].text
        # match_win = rank_tmp[4].text
        # match_draw = rank_tmp[5].text
        # match_lose = rank_tmp[6].text
        # goals = rank_tmp[7].text
        
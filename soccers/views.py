from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests,re

url = 'https://www.premierleague.com/match/93418'

response = requests.get(url)    #response 속성별로 정보가 담겨있는 덩어리
if response.status_code == 200: 

    soup = bs(response.text, 'html.parser') #beautifulsoap로 데이터 이쁘게 파싱

    # 크롤링한 데이터 텍스트파일로 만들어 확인하기
    with open('matchup_info.txt','w',encoding='utf-8') as file:
        file.write(soup.prettify())

    statssection = soup.select('.statsSection') #statsSection별로 변수에 정보 담기 (기본적으로 select, find는 자식요소까지 모두 함께 반환)
    stats =[]
    for section in statssection:
        cleaned_text = re.sub(r'\s+', ' ', section.text)  # 불필요한 공백, 줄바꿈, 탭 등을 한 칸의 공백으로 치환
        stats.append(cleaned_text)
    print(stats)



# Create your views here.
def matchup_info(request):
    url = 'https://www.premierleague.com/match/93418'

    response = requests.get(url)    #response 속성별로 정보가 담겨있는 덩어리
    if response.status_code == 200: 
        
        soup = bs(response.text, 'html.parser') #beautifulsoap로 데이터 이쁘게 파싱

        # 크롤링한 데이터 텍스트파일로 만들어 확인하기
        with open('matchup_info.txt','w',encoding='utf-8') as file:
            file.write(soup.prettify())

        statssection = soup.select('.statsSection') #statsSection별로 변수에 정보 담기 (기본적으로 select, find는 자식요소까지 모두 함께 반환)
        
        stats =[]
        for section in statssection:
            stats.append(section.text.strip())

        context ={
            'stats' : stats
        }
        return render(request,'soccers/matchup_info.html',context)
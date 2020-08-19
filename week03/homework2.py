from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#url loop돌려서 매일의 데이터 크롤링 할 수 있다.
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713'
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

genies = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for genie in genies:
    rank = genie.select_one('td.number').text[0:2].strip()
    # strip()을 먼저 제거하고 원하는 인덱스를 가져오기 -> text.strip()[0:2]
    title = genie.select_one('td.info > a.title.ellipsis').text.strip()
    artist = genie.select_one('td.info > a.artist.ellipsis').text

    doc = {
        'rank': rank,
        'title': title,
        'artist': artist
    }

    db.genie_2.insert_one(doc)

    print(rank,'위 :', title,'-',artist)
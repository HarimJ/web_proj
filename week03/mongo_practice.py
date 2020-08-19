import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         # a의 text를 찍어본다.
#         rank = movie.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
#         title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
#         star = movie.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
#         doc = {
#             'rank': rank,
#             'title': title,
#             'star': star
#         }
#         # print(doc)
#         # print(rank, title, star)
#
#         # db에 정보 넣기
#         db.movies.insert_one(doc)


# < 한개의 star 값을 출력하는 방법 3가지 >
# 1) 조건없이 find => list
# movies = list(db.movies.find({}))
# for movie in movies:
#     if movie['title'] == '월-E':
#         print(movie['star'])

# 2) 조건 + find => list
# 하나밖에 없는 게 확실합니다.
# movies = list(db.movies.find({'title': '월-E'}))
# print(movies[0]['star'])
# 리스트 형태니까 출력해도 하나만나온다

# 3) 조건 + find_one => dictionary
# movie = db.movies.find_one({'title': '월-E'})
# print(movie['star'])

# find_one을 할때는 한개의 확실한 조건을 알아야 한다.
# movie= db.movies.find_one({'star':'9.41'})
# print(movie['title'])

# 월-E와 같은 평점인 영화 이름 출력하기
my_movie = db.movies.find_one({'title':'월-E'})
my_movie_star = my_movie['star']
# print(my_movie_star)

movie = list(db.movies.find({'star': my_movie_star}))
# print(movie)

for target in movie:
    print(target['title'])

#--------------------튜터님 방법----------
# # 1)
# print('first')
# movies = list(db.movies.find({}))
# target_score1 = '0'
# for movie in movies:
#     if movie['title'] == '월-E':
#         target_score = movie['star']
# for movie in movies:
#     if movie['star'] == target_score:
#         print(movie['title'])
# # 2)
# print('second')
# movies = list(db.movies.find({}))
# target = db.movies.find_one({'title': '월-E'})
# target_score2 = target['star']
# for movie in movies:
#     if movie['star'] == target_score2:
#         print(movie['title'])
# # 3)
# print('third')
# movies = list(db.movies.find({}))
# target = list(db.movies.find({'title': '월-E'}))
# target_score3 = target[0]['star']
# for movie in movies:
#     if movie['star'] == target_score3:
#         print(movie['title'])

#----------------------------------------------------


# '월-E'의 평점과 같은 평점의 영화 제목들의 평점을 0으로 만들기

db = client.dbsparta_ninework

# my_movie = db.movies.find_one({'title' : '월-E'})
# my_movie_star = my_movie['star']

db.movies.update_many({'star': my_movie_star}, {'$set': {'star': '0'}})
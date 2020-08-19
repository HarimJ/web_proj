import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)
# 다른 방법
#url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716'
#data = requests.get(url,headers=headers)


# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
#parser : 내가 원하는 방식으로 변형 해주는 것 (파싱)

#############################
# (입맛에 맞게 코딩)
#############################

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    #태그 안의 텍스트를 찍고 싶을 땐 → 태그.text
    #태그 안의 속성을 찍고 싶을 땐 → 태그['속성']
    # movie 안에 a 가 있으면,
    rank = movie.select_one('td.ac > img')
    title = movie.select_one('td.title > div > a')
    score = movie.select_one('td.point')

    # a_tag = movie.select_one('td.title > div > a[href = "주토피아"]')
    # a의 text를 찍어본다.
    # print(a_tag.text)  <- if문 안했을때는 왜 작동하지 않는지 ? : 맨 처음 찾은 애가 text 형태가 아니여서 나오지 않는다 (못찾아서)
    '#old_content > table > tbody > tr:nth-child(2) > td.title > div > a'
    # copy selector 로 파싱한거 (위)

    if rank is not None:
        print(rank['alt'], title.text, score.text)
        #print(title.text)
        #print(title['title']) 로해도 제목이 나온다.
        #print(score.text)
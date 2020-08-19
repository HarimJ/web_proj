from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    url_reveice = request.form['url_give']
    comment_reveice = request.form['comment_give']
    print("===================================")
    print(url_reveice, comment_reveice)

    # 2. meta tag를 스크래핑하기
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_reveice, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]').get('content')
    og_title = soup.select_one('meta[property="og:title"]').get('content')
    og_description = soup.select_one('meta[property="og:description"]').get('content')

    # print(og_image)
    # print(og_title)
    # print(og_description)

    doc = {
        'url':url_reveice,
        'comment': comment_reveice,
        'og_image': og_image,
        'og_title': og_title,
        'og_description': og_description
    }

    db.memos.insert_one(doc)

    # 3. mongoDB에 데이터 넣기
    return jsonify({'result': 'success', 'msg': '저장 완료!'})


@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    memos = list(db.memos.find({}, {'_id': False}))
    print('+++++++++++++++++++++++++++')
    print(memos)
    # 2. articles라는 키 값으로 articles 정보 보내주기
    return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!', 'memos': memos})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

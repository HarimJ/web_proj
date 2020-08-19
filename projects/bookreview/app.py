from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.bookReview  # 'dbsparta'라는 이름의 db를 만듭니다.


# HTML을 주는 부분
# 기본 홈페이지
@app.route('/') # 기본적으로 get이 생략된것
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    # 1. 클라이언트가 준 title, author, review 가져오기.
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']
    print('==========================================')
    print(title_receive, author_receive, review_receive)

    # 2. DB에 정보 삽입하기
    db.reviews.insert_one({
        'title': title_receive,
        'author': author_receive,
        'review': review_receive
    })
    # 아니면 doc을 만들어서 넣기

    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({},{'_id': False}))
    print(reviews)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!', 'review': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

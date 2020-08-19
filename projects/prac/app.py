from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


# index.html 파일을 불러오기 <- 서버 받기
@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')


# API 역할을 하는 부분
# get
@app.route('/test', methods=['GET'])
def test_get():
    name_receive = request.args.get('name')
    title_receive = request.args.get('title_give')
    food_receive = request.args.get('food')
    sport_receive = request.args.get('sport')
    print(name_receive,title_receive,food_receive,sport_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!입니다'})
    # json화 인 정보를  넣으면 출력해준다

# post
@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    food_receive = request.form['food']
    sport_receive = request.form['sport']
    print(title_receive,food_receive, sport_receive )
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

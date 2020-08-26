from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.journey


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/first.html', methods=['POST'])
def my_page():
    return render_template('first.html')

# 여러 다른 페이지에 내용을 한디비에 저장은 못하나?
def write_diary():
    first_receive = request.form['first']

    review = {
        'firstDiary': first_receive
    }

    db.reviews.insert_one(review)
    return jsonify({'result': 'success', 'msg':'저장되었습니다.'})

@app.route('/second.html')
def my_page():
    return render_template('second.html')


@app.route('/third.html')
def my_page():
    return render_template('third.html')


@app.route('/fourth.html')
def my_page():
    return render_template('fourth.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.journey


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fourth')
def diary_page():
    return render_template('fourth.html')

@app.route('/first')
def photo_page():
    return render_template('first.html')

@app.route('/second')
def list_page():
    return render_template('second.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


# @app.route('/diaries/<num>')
# def get_diary(num):
#     diary = db.reviews.find_one({'num': num})
#     return render_template('diary_' + num + '.html', diary=diary['content'])
#
#
# @app.route('/fourth', methods=['GET'])
# def my_page():
#     first_diary = db.reviews.find_one({'name': 'first'})
#     if first_diary is None:
#         return render_template('fourth.html')
#     else:
#         return render_template('fourth.html', first_diary=first_diary['content'])
#
#
# @app.route('/diary_1', methods=['POST'])
# def write_diary():
#     first_receive = request.form['first']
#     print(first_receive)
#
#     review = {
#         'name': 'first',
#         'content': first_receive
#     }
#
#     db.reviews.insert_one(review)
#     return jsonify({'result': 'success', 'msg': '저장되었습니다.'})





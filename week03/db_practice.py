from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

#client는 요청하는것 (서버요청)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다. localhoat는 주소인데 우리가 지금 연결해서 사용하니까 로컬호스트라고 씀
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 데이터를 생성합니다.
# db.users.insert_one({'name': '덤블도어', 'age': 116})
# db.users.insert_one({'name': '맥고나걸', 'age': 85})
# db.users.insert_one({'name': '스네이프', 'age': 60})
# db.users.insert_one({'name': '해리', 'age': 40})
# db.users.insert_one({'name': '허마이오니', 'age': 40})
# db.users.insert_one({'name': '론', 'age': 40})


# MongoDB에서 데이터 모두 보기
# all_users = list(db.users.find({}))
# # {} 조건을 넣는다. 빈칸이면 users 안에있는 모든걸 찾으라는 뜻
#
# print(all_users[0])  # 0번째 결과값을 보기
# print(all_users[0]['name'])  # 0번째 결과값의 'name'을 보기
#
# # for user in all_users:  # 반복문을 돌며 모든 결과값을 보기
# #     print(user)
#
# for user in all_users:  # 반복문을 돌며 모든 결과값을 보기
#     if user['age'] >= 60 :
#        print(user['name'])


# MongoDB에서 특정 조건의 데이터 모두 보기
# find를 할때는 모두 찾는 것으로, list를 꼭 써줘야 한다.
# same_ages = list(db.users.find({'age': 40}))
#
# for user in same_ages:  # 반복문을 돌며 모든 결과값을 보기
#     print(user)
#
# #find_one은 하나만 찾는것. 단 하나만 가져오는것.
# user = db.users.find_one({'name': '덤블도어'})
# print(user)
#
# #그 중 특정 키 값을 빼고 보기
# user = db.users.find_one({'name': '덤블도어'}, {'_id': False})
# False는 가져오지 말라는 뜻으로 출력할때 나오지 않는다
# print(user)

# update 하는 방법
# 오타가 많으니 이 줄을 복사해서 씁시다!
# db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 19}})
#
# user = db.users.find_one({'name': '덤블도어'})
# print(user)

# 삭제하는것
# db.users.delete_one({'name': '론'})
#
# user = db.users.find_one({'name': '론'})
# print(user)

# db.users.delete_one({'name': '해리'})
# user = db.users.find_one({'name': '해리'})
# print(user)

# db.users.delete_one({'name': '덤블도어'})
# user = db.users.find_one({'name': '덤블도어'})
# print(user)
#
# db.users.delete_one({'name': '맥고나걸'})
# user = db.users.find_one({'name': '맥고나걸'})
# print(user)

# db.users.delete_one({'name': '허마이오니'})
# user = db.users.find_one({'name': '허마이오니'})
# print(user)

# 마지막 남은 사람 출력
last_one = list(db.users.find({}))
print(last_one[0]['name'])
a_list = []  # 비어있는 리스트 만들기
a_list.append(1)  # 리스트에 값을 넣는다
print(a_list)

a_list.append([2, 3])  # 리스트에 [2,3]이라는 리스트를 다시 넣는다
print(a_list)

# print 로 값 확인해보기
# a_list의 값은? [1,[2,3]]
# a_list[0]의 값은? 1
# a_list[1]의 값은? [2,3]
# a_list[1][0]의 값은? 2

print(a_list[1])
print(a_list[1][1])


a_dict = {}  # 비어있는 딕셔너리 만들기

wizard = {'name': 'Harry Potter', 'age': 40}
print(wizard)

wizard['height'] = 173
print(wizard)

# print 로 값 확인해보기
# wizard의 값은? {'name':'Harry Potter','age':40, 'height':173}
# wizard['name']의 값은? 'Harry Potter'
# wizard['age']의 값은? 40
# wizard['height']의 값은? 173

wizards = [{'name': 'Harry Potter', 'age': 40}, {'name': 'Ron Weasley', 'age': 40}]
print(wizards)

# print 로 값 확인해보기
# wizards[0]['name']의 값은? 'Harry Potter'
# wizards[1]['name']의 값은? 'Ron Weasley'

new_wizard = {'name': 'Albus Potter', 'age': 14}
wizards.append(new_wizard)
print(wizards)

# print 로 값 확인해보기
# wizards의 값은? [{'name':'Harry Potter','age':40}, {'name':'Ron Weasley','age':40}, {'name':'Albus Potter','age':14}]
# wizards[2]['name']의 값은? 'Albus Potter'

def showPost():
    print("hello")
    print(wizards[1]['name'])

#실행할때는 들여쓰기 밖에서
showPost()

def sum_all(a,b,c):
    return a + b + c

def mul_all(d,e):
    return d * e

result = sum_all(11, 3, 6) + mul_all(3, 4)
print(result)

#---------------------------------------------------------------------------

def is_even(num):  # oddeven이라는 이름의 함수를 정의한다. num을 변수로 받는다.
    if num % 3 == 0:  # num을 2로 나눈 나머지가 0이면
        return '나머지가 0'  # True (참)을 반환한다.
    elif num % 3 == 1:
        return '나머지가 1'
    else:  # 아니면,
        return '나머지가 2'  # False (거짓)을 반환한다.

result = is_even(22)

# print 로 값 확인해보기
# result의 값은 무엇일까요?
print(result)

#---------------------------------------------------------
def is_adult(age):
    if age >= 20:
        print('성인입니다')  # 조건이 참이면 성인입니다를 출력
    else:
        print('청소년이에요')  # 조건이 거짓이면 청소년이에요를 출력

is_adult(30)
is_adult(10)
is_adult(19)


# 조건을 여러 개 사용하고 싶을 때
def check_generation(age):
    if age > 120:
        print('와 19세기에 태어나셨군요!')
    elif age >= 80:
        print('80세 이상! 인생은 여든부터!')
    elif age >= 60:
        print('인생은 60부터!')
    else:
        print('젊으시군요! 장래희망이 뭔가요?')


my_age = 60
check_generation(my_age)

#-------------------------반복문 ----------

fruits = ['사과', '배', '감', '귤']

for fruit in fruits:  # fruit 은 우리가 임의로 지어준 이름입니다.
    print(fruit)  # 사과, 배, 감, 귤 하나씩 꺼내어 출력합니다.


fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

count = 0
for fruit in fruits:
    if fruit == '배':
        count += 1   # count += 1

# 사과의 갯수를 출력합니다.
print(count)

# 배의 갯수를 출력하기
def printFruit():
    count=0;
    for fruit in fruits:
        if fruit == '배':
            count += 1
    return count     # print(count)

print(printFruit())  # function에 return 하면 출력할때 print 로 출력하고
                     # function에 print 하면 출력할때 그냥 함수 이름만 출력 -> printFruit()


# 이름 변수 주기 => name
def count_fruit(name):
    count=0;
    for fruit in fruits:
        if fruit == name:
            count += 1
    return count

print(count_fruit('감'))  # 출력할때 원하는 이름만 하고 싶을때


#----------------------------------------------------------------------
wizards = [
    {'name': '해리', 'age': 40},
    {'name': '허마이오니', 'age': 40},
    {'name': '론', 'age': 41},
]
# 모든 마법사의 이름과 나이를 출력
for wizard in wizards:
    print(wizard['name'], wizard['age'])

wizard  # 출력하기


# ___@@__ 중요__@@___
professor_wizards = [
    {'name': '덤블도어', 'age': 116},
    {'name': '맥고나걸', 'age': 85},
    {'name': '스네이프', 'age': 60},
]

# 이번엔, 반복문과 조건문을 응용한 함수를 만들어봅시다.
# 마법사의 이름을 받으면, age를 리턴해주는 함수
def get_age(name, wizards):
    # wizards! 윗 줄 함수 선언에서 사용한 변수죠? 함수 사용하는 쪽에서 쓰는 변수명 아닙니다!
    for wizard in wizards:
        if wizard['name'] == name:
            return wizard['age']
    return '해당하는 이름이 없습니다'

print(get_age('덤블도어', professor_wizards))
print(get_age('해리포터', professor_wizards))






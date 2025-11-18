
'''
my_tuple = (1,2,3,4)
print(my_tuple)

no_paren_tuple = 5,6,7
print(no_paren_tuple)

#출력에 () 소콸호가 있으면 tuple 이다. 라고 생각하면 된다.
#쉼표가 있어야 튜플인지 프로그램이 인식을 한다.
#언패킹 - 풀어 해쳐지는 기능(?)
#리스트와 튜플이 차이는 변경이 불가능
# 7페이지 해볼것
#인덱스라는 클래스는 첫번째 값만 반환 해준다. 튜플에서만
'''
'''
user = ("minji",25,"Seoul")

restored_user = ("eunji",) + user[1:]

print(restored_user)

name = restored_user[0]
age = restored_user[1]
city = restored_user[2]

name, age, city = restored_user

print(name, age, city)

temp12 = (name,age,city)

print(temp12)

#SET
#{} 중괄호로 사용하나.
#크기를 제한을 한다.

A = {1,2,3}
B = {4,5,6}

print(A|B)
print(A.union(B))

print(A & B)
print(A.intersection(B))

print(A - B)
print(A.difference(B))

print(A ^ B)
print(A.symmetric_difference(B))

submissions = ['kim','lee','kim','park','choi','lee','lee']
submission1 = set(submissions)
print(f"""제출한 학생 수 : {len(submission1)}
제출자 명단 : {submission1}""")

#dict
#검색시 문자열로 사용한다.
#듀플이 2개 값이 저장이 되어 있으면 딕션어리로 변환이 가능하다.
#기호는 {}
# % 오류가 나면 프로그램 정지 한다.!!!
#get() 매소드 사용시 검색을 하고 없으면 오류를 반환하지 않는다.

#keys() 모든 키를 반환 해준다.
#values() 모든 값은 반환 해준다.
#items() 모든 키,값은 반환 해준다.
'''
'''
#실습1

user_key = ["username", "email", "level"]
user_value = ["skywork", "sky@example.com",5]

user = dict(zip(user_key, user_value))

print(user)

email_value = user.get("email")
#email_value = user["email"]
print(email_value)

user["level"] = 6
#user.update({"level"}) = 6
print(user)

phone = user.get("phone", "미입력")
print(phone)

user.update({"nickname" : "sky"})
print(user)

del user["email"]
print(user)

user.setdefault("signup_date", "2025-07-01")
print(user)

#실습2
students = {}
students = [(Alice : 85), ]


'''

#파이선은 조건식은 들여쓰기 즉 여백으로 구분하기 때문에 조심해서 사용해야 한다.
'''
a = int(input())
if a > 10:
    print("a는 10보다 커요")
print("조건문 종료")
'''
'''
a = input()
if a == "맑음" : 
    print("선크림을 바르세요!")

if a == "비" :
    print("우산을 챙기세요")
'''
'''
age = 15
if age >= 18 : 
    print("성인입니다.")
else : 
    print("미성년자입니다.")
    
# else는 추가적으로 조건을 만들수 없다.
#다른 명령어가 있다. elif

number = int(input("정수를 입력해주세요 : "))

if number % 2 == 0 :
    print("짝수 입니다.")
else : 
    print("홀수 입니다.")
    
'''
'''
age = int(input("나이를 적어주세요 : "))
if age <= 12 : 
    print("전체 관람가 입니다.")
elif 12 < age <= 15 :
    print("12세 이상 관람가 입니다.")
elif 15 < age <= 18 : 
    print("15세 관람가 입니다.")
else : 
    print("청소년 관람불가 입니다.")
'''
# 다중 조건은 위 조건을 검색된 결과가 도출이 되면 도출된 값으로 하위 조건에서 판별을 한다.

김밥 = 2500
삼각김밥 = 1500
도시락 = 4000

money = int(input("돈을 넣어 주세요 : "))
manu_select = input("메뉴를 선택해 주세요 (김밥, 삼각김밥, 도시락) : ")

if manu_select == "김밥" : 
    if money >= 김밥 : 
        print("김밥을 구매 하셨습니다.")
        money -= 김밥
    else : 
        print("잔액이 부족합니다.")
elif manu_select == "삼각김밥" : 
    if money >= 삼각김밥 :
        print("삼각김밥을 구매하셨습니다.")
        money -= 삼각김밥
    else : 
        print("잔액이 부족합니다.")
elif manu_select == "도시락" : 
    if money >= 도시락 : 
        print("도시락을 구매하셨습니다.")
        money -= 도시락
    else : 
        print("잔액이 부족합니다.")
else : 
    print("선택한 메뉴가 없습니다.")
'''
#for문에 대해서.

fruits = ['apple', 'banana','cherry']
for fruit in fruits : 
    print(f"I like {fruit}")
    
text = 'hello'
for ch in text : 
    print(ch)
    
person = {"name" : "Alice" , "age" : 30}
for key in person :
    print(key)
    
for value in person.values() : 
    print(f"Value : {value}")
    
for key, value in person.items() : 
    print(f"{key} => {value}")
'''
# for문에서 리스트 값은 불러오면 저장이 되어진 value 값이 불러온다.
# 문자열을 불러 오게 되면 하나하나 분리 되어 저장이 된다.
# 튜플에서는 for문으로 불러오면 해당 검색어가 key 값이 되어 value값을 변환한다.
# key값과 value값 불러 오기 위해서는 변수.items() 라고 붙여 사용한다.
'''
numbers = [3,6,1,8,4]
temp = []
for x in numbers :
    temp.append(x * 2)
print(temp)
#변수.append() 리스트 값에 추가 하여 저장하는 메소드 이다.
    
words = ["apple", "banana","kiwi","grape"]
words1 = []
for x in words : 
    words.append(len(words))
print(words1)
# 메소드 len() 들어가 있는 자료가 몇개가 있는지 확인 하여 숫자로 반환해 준다.

coordinates = [(1,2), (3,4),(5,6),(7,8)]
x_values = []
y_values = []
'''
#리스트에 튜플형태의 자료로 만들어 하나하나 불러 오는 값을 계산하는 문제이다.
# 못풀었다.

'''
for i in range(1,20,3) : 
    print(i)

input12 = int(input("숫자를 입력해 주세요 : "))
value = ()
for tmp in range(1,input12+1) : 
    tmp += tmp
    value = tmp
print(value)

for tmp in range(1,10) : 
    print(f"{input12} * {tmp} = {input12 * tmp}")
 
value11 = 0    
for tmp in range(1,101,3) : 
    value11 = tmp + value11

print(value11)
value22 = 0
for tmp in range(1, input12+1) : 
    if(tmp % 2 == 0) : 
        if(tmp % 5 == 0) : 
            value22 = value22 + tmp
print(value22)
'''
'''
colors = ['red','blue']
fruits = ['apple','banana']

for color in colors : 
    for fruit in fruits : 
        print(f'{color} {fruit}')
        
'''
'''
number = 0

for tmp1 in range(2,10) :
    print(f"[ {tmp1}단 ]")
    for tmp2 in range(1,10) :
        print(f"{tmp1} * {tmp2} = {tmp1 * tmp2}")

star = 0
star_input = int(input("숫자를 입력해 주세요"))

for tmp1 in range(1,star_input+1) : 
    print(f"*" * tmp1)
    

for tmp1 in range(1,star_input + 1) : 
    for tmp2 in range(1,star_input +1) : 
        print(f" "*tmp2,"*"*tmp1,end="")
'''
'''
n=10
temp = 0
squares1 = []
for tmp1 in range(1,n) : 
    temp = tmp1**2
    squares1.append(temp)
    
print(squares1)

temp = 0

squares2 = [x**2 for x in range(1,n)]
print(squares2)


n=50
squares3 = []
for tmp in range(1,n) : 
    if tmp % 3 == 0 :
        squares3.append(tmp)
        
print(squares3)

squares4 = [tmp for tmp in range(1,n) if tmp % 3 == 0]
print(squares4)

fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]
fruits_all = []
for fruit in fruits :
    if len(fruit) > 5 : 
        fruits_all.append(fruit)
print (fruits_all)
        
fruits_all = []
fruitss = [fruit for fruit in fruits if len(fruit) > 5]
print(fruitss)
'''
'''
secret_code = "test"
secret_input = ""


while secret_code != secret_input :
    secret_input = input("비밀코드를 입력하세요 : ")
    if secret_input != secret_code : 
        print("비밀코드가 틀렸습니다. 다시 시도해 주세요")
print("입장하셨습니다.")
'''
'''
# while 문으로 변환
for tmp1 in range(2,10) :
    print(f"[ {tmp1}단 ]")
    for tmp2 in range(1,10) :
        print(f"{tmp1} * {tmp2} = {tmp1 * tmp2}")
'''

'''
tmp_input = int(input("입력해 주세요 : "))
tmp1 = 1
tmp2 = 1  
while tmp1 != tmp_input+1:
    while tmp2 != 10 :
        print(f"{tmp1} * {tmp2} = {tmp1 * tmp2}")
        tmp2 += 1
    tmp2 = 1
    tmp1 += 1
print("완료 되었습니다.")
'''
weather = str(input("비 또는 맑음 중 선택 해주세요 : "))

if weather == "비" : 
    print("우산을 챙기세요")
elif weather == "맑음" : 
    print("선크림을 바르세요!")
else : 
    print("잘못입력하셨습니다.")
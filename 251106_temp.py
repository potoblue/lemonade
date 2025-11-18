name = "코딩오울"
age = 15
mbti = "ENFP"
print(f"""안녕하세요.
제 이름은 {name},
{age}살입니다.
제 MBTI는 {mbti}에요.""")

# print 연산자에는 한줄로 표시할수 있는 방법과 다중 줄로 표시 하느 방법이 있다.
# 단줄 표기시에는 print()쓰면 된다.
# 다중줄을 표기시에는 print(f"""  """)으로 표기 해야 한다.  
# 변수를 넣어 표시 할때는 {}사용한다.
# 단 변수 사용시 print(f""" """")사용해야 한다.
# print() 사용시 에러가 발생이 되는 것을 확인 하였다.


# 연산자 값과 값 사이에 연산을 수행하는 기호
# 다항 보다는 단항 연산자가 우선순위가 높다.
# 산술 연산자 : +, -, *, /, // : 몫, % : 나머지, **

#print(7 % 3)  # 나머지
#print(7 // 3) # 몫
#print(2 ** 3) # 제곱

# 프로그램 처리 순서는 위에서 아래로 왼쪽에서 오른쪽으로

a = 3
print(a)
a += 3
print(a)

# a = a + 1 과 a += 1 과 같은 값이 도출이 된다.
# 프로그래머 편리에 의해 개발이 되었다.


result =  2 + 3 * 4
print(result)
result = (2 + 3) * 4
print(result)
# 연산자의 우선순위에 대한 문제이다.


용돈, 책값, 점심값, 과외 = 300000, 80000, 9000, 120000
잔금 = 용돈 - 책값 - (점심값 * 5) + 과외
남은금액 = (잔금 + (잔금 * 0.2)) * (1/3)
print(남은금액)
# 연습문제이다.


#intro += drop
#intro += intro
#print(intro)
intro = "둠칫"
drop = "두둠칫"
#intro += drop
#intro += intro
#print(intro)
print((intro+drop)*2)
# 자신의 

name = input("이름을 입력하세요 : ")
print("안녕하세요, ", name)


a = int(input())
b = int(input())
print(a + b)


e = bool(int(input())) #부울 대수 정확히 출력하기 위해서는 형을 변환후 적용해야 한다.
print(e)


과일1, 과일2, 과일3 = input().split(",")
print (과일1, 과일2, 과일3)


"""
#split 다중 입력을 할때 구분을 어떤 문자로 할것인지 정하는 명령어

#name, age = input("이름과 나이를 입력하세요 : ").split(",")
#print(f"안녕하세요. 저는 {name}이고, {age}살 입니다.")
"""
number = int(input())


첫번째 = number // 1000
print(첫번째)
두번째 = (number % 1000) // 100
print(두번째)
세번째 = (number % 100) // 10
print(세번째)
네번째 = number % 10
print(네번째)
"""
"""
리스트이름1 = []

리스트이름2 = ["저장할 자료1", "저장할 자료2", "저장할 자료3"]

리스트이름3 = [10, "hello", 3.14, [1,2,3]]

test_list = list()
test_list2 = ("CodingOn")
print(리스트이름1)
print(리스트이름2)
print(리스트이름3)


text = list("Python")
print(text[0])
print(text[3])
print(text[-1])
print(text[-3])

text[0] = "F"
print(text[0])


#1
nums1 = [10,20,30,40,50]
print(nums1[4:])

#2
nums2 = [100,200,300,400,500,600,700]
print(nums2[2:5])

#3
nums3 = [1,2,3,4,5]
nums3[0] = nums3[0]*2
nums3[1] = nums3[1]*2
nums3[2] = nums3[2]*2
nums3[3] = nums3[3]*2
nums3[4] = nums3[4]*2
print(nums3[:])

#4
items = ["a","b","c","d","e"]
print(items[::-1])

#5
data = ["zero", "one","two","three","four","five"]
data1 = list()
data1
print(data1[:])


'''
item_name = ["삼각김밥", "김밥", "도시락"]
item_price = [1500,2500,4000]

item = dict(zip(item_name, item_price))
money = int(input("돈을 넣어 주세요 : "))
item_selete = input("김밥, 삼각김밥, 도시락중 선택해 주세요 : ")

if item_selete in item :
    if money >= item.get(item_selete) :
        money -= item.get(item_selete)
        print(f"{item_selete} 선택하셨습니다. 잔액은 {money} 입니다.")
    else : 
        money = (money - item.get(item_selete)) * -1
        print(f"{item_selete} 선택하셨고 금액은 {money} 부족합니다.")
else : 
    print("세가지 메뉴중에 선택을 되지 않았습니다.")
'''

'''
if item_selete == "김밥" : 
    if money >= item.get("김밥") : 
        money -= item.get("김밥")
        print(f"김밥을 선택하셨습니다. 잔액은 {money} 입니다.")
    else : 
        print("잔액이 부족합니다.")
if item_selete == "삼각김밥" : 
    if money >= item.get("삼각김밥") : 
        money -= item.get("삼각김밥")
        print(f"삼각김밥을 선택하였습니다. 잔액은 {money} 입니다.")
    else : 
        print("잔액이 부족합니다.")
if item_selete == "도시락" : 
    if money >= item.get("도시락") : 
        money -= item.get("도시락")
        print(f"도시락을 선택하셨습니다. 잔액은 {money} 입니다.")
    else : 
        print("잔액이 부족합니다.")
else : 
    print("잘못입력하셨습니다.")
'''
'''
a = -3.14
print(type(a))
print(int(a))
'''
'''
#cnt1 = "(()"
#cnt2 = 0
# 단일 괄호 검사
def check_parentheses(s) : 
    tmp = 0
    for i in range(len(s)) : 
        if s[i] == "(" and tmp >= 0: 
          tmp += 1
        elif s[i] == ")" and tmp >= 0 : 
            tmp -= 1          
    if tmp == 0 : 
        return True
    if tmp != 0 :
        return False 
print(check_parentheses("(())"))
print(check_parentheses("(()"))
print(check_parentheses("())("))

# 연속문자 압축
tmp1 = ""
tmp2 = ""
def compress(s) : 
    global tmp1, tmp2
    for i in range(len(s)) : 
        if i == 0 :
            tmp1 = s[0]
            tmp2 = s[0]
        
        if tmp1 != s[i] :
            tmp1 = s[i]
            tmp2 = tmp2 + tmp1
            
    return tmp2
    print(compress("aaaabbbbccfcdddeee"))
'''

# class Asset : 
#     def __init__(self, name, cost):
#         self.name = name
#         self.cost = cost
        
#     def print(self) : 
#         print(f"자산 : {self.name}, 현재 비용 : {self.cost}원")
            
# class Equipment (Asset):
#     def __init__(self, name, cost, depreciation):
#         super().__init__(name, cost)
#         self.depreciation = depreciation
    
#     def print(self) : 
#         print(f"자산 : {self.name} , 현재 비용 : {self.cost * (1-self.depreciation)}원")

# class Vehicle (Asset):
#     def __init__(self, name, cost, premium):
#         super().__init__(name, cost)
#         self.premium = premium
        
#     def print(self) :
#         if self.cost <= 10000 : 
#             print(f"자산 : {self.name}, 현재 비용 : {self.cost}")
#         else : 
#             print("최소 비용(10,000원) 미만입니다.") 
#         print(f"{self.name}의 연간 가치 : {self.cost - self.premium}")
        
# server = Equipment("고성능 서버", 500000, 0.15)
# server.print()
# server.cost = 450000
# server.print()
# company_car = Vehicle("업무용세단", 3000000,300000)
# company_car.print()
# company_car.cost = 5000

#asset_list = [server, company_car]

# import numpy as np

# arr = ([1,2],[3,4],[5,6])
# print(arr)

# print(np.ones((2,2)))
# print(arr)

#comprehansion
#제곱근 리스트 만들기
comprehansion = [x**2 for x in range(1,11)]
print(comprehansion)
# 3의 배수만 리스트로 만들기
#compreList = [x % 3 == 0 for x in range(1,11)]
#print(compreList)
#3의 배수로 True False로 표현 해준다.
compreList = [x for x in range(1,11) if x % 3 == 0]
print(compreList)
#문자열 리스트에서 길이가 5 이상인 단어만 뽑기

fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "ornage"]
fruitList = []
for x in range(len(fruits)) : 
    if len(fruits[x]) >= 5 : 
        fruitList
        
print(fruitList)
print(len(fruits[0]))        


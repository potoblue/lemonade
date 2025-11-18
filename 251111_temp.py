'''def greet() : 
    print("hello, World")
    
greet()
'''
'''
def greet(name) : 
    print(f"Hello, {name}")
    
greet("CodingOwl")

def add(a,b) : 
    return a + b

result = add(3,5)
print(result)
'''

'''
def calculate(a, b, operator) : 
    if operator == "+" : 
        return a + b
    elif operator == "-" : 
        return a - b
    elif operator == "*" : 
        return a * b
    elif operator == "/" : 
        return a / b
    else : 
        return "---"

print(calculate(3,2,"+"))
'''
'''
def average(*args) : 
    return sum(args) / len(args)

print(average(1,2,3,4,5))


def longgest(*args) : 
    if len(agrs) == 0 :
        return print("No arguments provided")
    
    maxString = ""
    for arg in args : 
        maxsize = 0
        if len(arg) > len(maxString) : 
            max
'''
'''
def print_info(**kwargs) : 
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
def discount_price(**kwargs) : 
    for key, value in kwargs.items() :
        discounted = value * 0.9
        print(f"{key} : 할인가 {discounted} (원가 {value})")
        
discount_price(apple = 2000, watermelon = 20000, chocoleta = 2500)
'''
'''
current_user = []

def login(name) : 
    if len(current_user) == 0 : 
        print(f"{name}님 로그인 성공")
        current_user.append(name)
    else :
        print("이미 로그인되어 있습니다.")

def logout() : 
    current_user.pop()

login("aaa")
login("ccc")
logout()
login("bbb")
print(current_user)
#여러번 시도하는 횟수 미 구현
'''
'''
def recursive_func(n) : 
    if n == 0 : 
        return
    
    print("재귀호출", n)
    recursive_func(n-1)
    
recursive_func(5)
'''
'''
n=4
tmp = []
for i in range(1,n+1) : 
    tmp.append(i*(i+1))
    print(tmp)
'''
'''
def factorial(n) : 
    i = 1
    for j in range(1, n+1): 
        j *= i
    return i

facts = factorial(4)
print(facts)
'''
'''
i = 0
def factorial(n) : 
    global i
    if n == 1 : 
        i = 1
        return i
    else : 
        t = factorial(n-1)
        i *= t 
        return
factc = factorial(4)
'''
'''
def factorial(n) : 
    tmp = 0
    if n == 0 : 
        return
    #print("ㅇㅇㅇ",n)
    print(tmp)
    factorial(n-1)
    
    
factorial(2)
'''

add = lambda a,b : a+b
print(add(3,4,))
print((lambda a,b: a + b)(3,4))
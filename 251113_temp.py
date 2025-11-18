# from abc import ABC, abstractclassmethod

# class Payment(ABC) :
     
#     @abstractclassmethod
#     def pay(self) : 
#         pass
    
# class CardPayment(ABC) : 
#     def pay(self, amount) : 
#         print(f"CardPayment")

# f = open("example.txt", "w", encoding="utf-8")

# f.write("파이썬 파일 입출력 예제 입니다. \n")
# f.write("이 파일은 write()로 작성 되어습니다. \n")

# f.close()

# f = open("example.txt","r", encoding="utf-8")
# #content = f.readline()
# content = f.readlines()
# print(content)
# f.close()

# with open('../my_math/with_example.txt', 'a', encoding="utf-8") as f:
#     while True : 
#         text = input("저장할 내용을 입력해 주세요(종료 -z) : ")
#         if text == 'z' or text == 'Z' : 
#             break
#     f.write(text)
#     f.write('\n')

# test = [1,2,3,4,5]

# try :  
#     print(test[10])
# except IndexError as a : 
#     print(a)


class Temperature : 
    def __init__(self, celsius):
        self._celsius = celsius
        
    @property
    def celsius(self) : 
        return self._celsius
    
    @celsius.setter
    def celsius(self,value) : 
        if value < -275.15 : 
            raise ValueError("절대 0도 이하일 수 없습니다.")
        self._celsius = value
        
t = Temperature(25)
print(t.celsius)
t.celsius = 30
print(t.celsius)


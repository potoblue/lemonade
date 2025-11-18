'''
print(type(10))
print(type([1,2,3,4,5]))

class Person : 
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        
    def introduce(self) : 
        print(f"안녕하세요. 저는 {self.name}, {self.age} 살입니다.")
        
person1 = Person("지민", 25)
person2 = Person("민준", 30)

person1.introduce()
person2.introduce()

class Book : 
    def __init__(self, title, author, total_pages, current_page):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page
        
    def read_page(self,pages) : 
        self.current_page = pages
        if self.current_page > self.total_pages : 
            self.current_page += self.read_page(pages)            
    def progress(self) : 
        percent = (self.current_page / self.total_pages) * 100
        print(f"{percent:.1f}")
            
book1 = Book("넥서스" , "아무개", 500, 0)
print(book1.current_page)
print(book1.read_page(100))
print(book1.current_page)
print(book1.read_page(10))
print(book1.current_page)

class Rectangle : 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self) : 
        print(f"{self.width * self.height}")
        
rectangle1 = Rectangle(10,10)
rectangle1.area()
'''
'''
class User:
    total_users = 0
    def __init__(self, username, points):
        self.username = username
        self.points = points
        User.total_users += 1

    def add_points(self, amount):
        self.points += amount
    
    def get_level(self):
        if self.points >= 500:
            return "Gold"   
        elif self.points >= 100:
            return "Silver"
        else:
            return "Bronze"
    @classmethod
    def get_total_users(cls):
        print(f"총 유저 수: {cls.total_users}")
 
u1 = User("Alice", 150)
u2 = User("Bob", 50)
u3 = User("Charlie", 600)
u34 = User("Charl2ie", 600)
print(u1.username)
print(u1.get_level()) 

User.get_total_users()
'''
'''
class User:
    total_users = 0
    def __init__(self, username, points):
        self.__username = username
        self.points = points
    
    def set_username(self, username) : 
        self.__username = username
    
    def get_username(self) : 
        return self.__username

    def add_points(self, amount):
        self.points += amount


u1 = User("alll", 150)
print(u1.__username)

'''
'''
class UserAccount : 
    def __init__(self, username, password) :
        username = "admin"
        password = 2134
        self.username = username
        self.__password = password
        
    def     
    
    def change_password(self, old_pw, new_pw) : 
        pass
'''
'''
class Animal : 
    def speak(self) : 
        print("동물이 소리를 냅니다.")
        
class Dog(Animal) :
    pass

d = Dog()
d.speak()
'''
'''
class Animal : 
    def speak(self) : 
        print("동물의 소리를 냅니다.")
class Cat(Animal) : 
    def speak(self, sound):
        print(sound)
        
c = Cat()
c.speak()
'''
class Shape :
    def __init__(self, sides, base):
          self.sides = sides
          self.base = base
    def printInfo(self) : 
        self.sides = 4
        self.base = 10
        tmp1 = self.sides
        tmp2 = self.base
        print(f"""변의 개수 : {tmp1}
              밑변의 길이 : {tmp2}""")
    def area(self) : 
        print("넓이 계산이 정의되지 않았습니다.")
        
class Rectangle(Shape) : 
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height
        
    def area(self) : 
         return self.base * self.height
     
class Triangle(Shape) : 
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height
    
    def area(self) : 
        return (self.base * self.height) /2
    


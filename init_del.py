#생성자와 소멸자 (Constructor & Destructor)

#__init__: All classes have a function called __init__(), which is always executed when the class is being initiated (초기화 메서드)
#self: A reference to the current instance of the class, and is used to access variables that belong to the class
#(self는, 이름이 반드시 self일 필요는 없으나 암묵적으로 self를 쓸 것을 권장한다. 그리고 반드시 첫 번째 parameter로 들어와야 한다)


#init 메서드는 바로 실행된다
class Book:
    def __init__(self):
        print('새 책입니다!')

Book()     #새 책입니다! 

#추가 예시 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(x):
        print('Hello everyone! Nice to meet you!')


P1 = Person('Anne', 20)
P1.age = 40     #age = 40으로 변경된다 

print(f'내 이름은 {P1.name} 입니다.')
print(f'나는 {P1.age}살 입니다.')
P1.myfunc()



#__del__: 소멸자 메서드, a finalizer which is called when an object is garbage collected 

class Unit:
    def __init__(self):
        print('__init__실행 완료')

    def __del__(self):
        print('__del__실행 완료')

Unit()      #__init__, __del__ 두 개 모두 실행됨 
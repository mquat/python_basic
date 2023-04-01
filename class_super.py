class Person:
    def __init__(self):
        self.hello = '안녕하세요'

class Student(Person):
    def __init__(self, name):
        super().__init__()  #call __init__ from parent class
        self.introduction = f'제 이름은 {name}입니다.'


james = Student('james')
print(james.hello)
print(james.introduction)

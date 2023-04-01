#아래와 같이 구현하면, 원래 기능을 유지하면서 메소드 오버라이딩 가능

class Person:
    def greeting(self):
        print('안녕!')

class Student(Person):
    def greeting(self):
        super().greeting()  #부모 클래스의 메서드 호출. 이게 없으면 Student는 부모 클래스의 메서드를 무시하고 본인의 메서드로 오버라이딩
        print('나는 고1 학생이야!')

emma = Student()
emma.greeting()
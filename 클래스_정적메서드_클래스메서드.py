#static method: 인스턴스 속성이나 인스턴스 메서드가 필요 없을 때 사용
class Calc:
    @staticmethod
    def add(a,b):
        print (a + b)
    

Calc.add(2,3)
Calc.add(20,30)


#class method: 클래스 속성을 매개변수로 받아서 사용
class Person:
    count = 0 

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):   #인스턴스 발생할 때마다 해당 인스턴스를 호출, 접근
        print(cls.count)

james = Person()
emma = Person()
Person.print_count()    #return 2


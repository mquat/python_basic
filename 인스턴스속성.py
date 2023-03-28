#속성: 클래스 속성과 인스턴스 속성

#인스턴스 속성 -> 인스턴스 별로 독립, 각 인스턴스가 값을 따로 저장해야할 때 사용
class Person:
    def __init__(self):
        self.hobbies = []

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)

emma = Person()
emma.add_hobby('singing')
emma.add_hobby('drawing')

james = Person()

print(emma.hobbies)
print(james.hobbies)    #빈 list만 출력된다
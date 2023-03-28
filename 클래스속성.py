#속성: 클래스 속성과 인스턴스 속성

#클래스 속성 -> 클래스 자체에 속하는 속성, 따라서 모든 인스턴스에 공유됨 (인스턴스 모두가 사용해야 하는 값을 저장할 때 사용)
class Person:
    hobbies = []

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)

emma = Person()
james = Person()

emma.add_hobby('singing')
emma.add_hobby('drawing')

print(emma.hobbies)
print(james.hobbies)    #james도 singing/drawing이 동일하게 출력된다

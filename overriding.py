#예시 출처 - https://wikidocs.net/16073

class Country:
    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')

#------------------------------------------------
#오버라이딩 1 - general(superclass로부터 상속받은 show()를 오버라이딩해서 사용)

class Korea(Country):
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        print(
            """
            국가의 이름은 {}입니다.
            국가의 인구는 {}입니다.
            국가의 수도는 {}입니다.
            """.format(self.name, self.population, self.capital)
        )

a = Korea('대한민국', '5천만명', '서울')
a.show()


#------------------------------------------------
#오버라이딩 2 - super() 이용 
#super() 를 사용하면, superclass의 show()도 실행시키고, 오버라이딩한 show()도 실행시킨다 

class Korea(Country):
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        super().show()  
        print(
            """
            국가의 이름은 {}입니다.
            국가의 인구는 {}입니다.
            국가의 수도는 {}입니다.
            """.format(self.name, self.population, self.capital)
        )

a = Korea('대한민국', '5천만명', '서울')
a.show()


#------------------------------------------------
#오버라이딩3 - 다중상속 (파이썬은 C++과 같이 다중상속이 가능)
#예시 참고: https://dojang.io/mod/page/view.php?id=2388

class Person:
    def greeting(self):
        print('지금부터 학생 소개가 있겠습니다.')
        print('이름: 홍길동')

class University:
    def manage_credit(self):
        print('학교: IT대학교')
        print('학점: 4.0/4.5')

class Undergraduate(Person, University):
    def manage_activity(self):
        print('동아리: 코딩학회')

student1 = Undergraduate()
student1.greeting()
student1.manage_credit()
student1.manage_activity()


#------------------------------------------------
#오버라이딩4 - 다이아몬드 상속 = 죽음의 다이아몬드, 어떤 메소드를 호출해야 할지 애매한 상태
#예시 참고: https://dojang.io/mod/page/view.php?id=2388

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B,C):
    pass

x = D()
x.greeting()    #안녕하세요. B입니다. 

#mro(): 메서드 탐색 순서(method resolution order), 기본적으로 다중상속에서는 left to right으로 메소드를 탐색한다. 
print(D.mro())


#------------------------------------------------
#번외 - object 클래스는 모든 클래스의 조상 
#예시 참고: https://dojang.io/mod/page/view.php?id=2388

print(int.mro())    #class 'int', class 'object'

#파이썬2와 달리, 파이썬3에서는 object를 생랼한다. 아래 2개 코드는 서로 동일한 내용이다. 
class X:
    pass

class X(object):
    pass 
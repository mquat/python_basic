#예시 출처 - https://wikidocs.net/16073

class Country:
    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')

class Korea(Country):
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'국가 이름은 {0}입니다.', self.name)


#------------------------------------------------
#오버라이딩 1 - general

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
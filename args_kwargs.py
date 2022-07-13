#args: 가변인자(인자의 개수가 변할 수 있는데 몇 개로 변할지 모를 때), tuple 반환
#kwargs: keyword 가변인자, dict 반환


#args 예시
def num(*args):
    print(args)

def add(*args):
    result = 0 
    for num in args:
        result += num 
    print(result)

num(1,2,3)
num(5,6,7,8,9,10)

add(1,5,10)
add(100,1)


#kwargs 예시
def introduce(**kwargs):
    print(kwargs)

def introduceEnglish(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")

introduce(name="Emma", age="20", city="Seoul")
introduceEnglish(My_name='Emma!')
#pure function(순수 함수): 함수의 실행이 외부 상태에 영향을 끼치지 않음, 비상태, no side effect, 변수를 최대한 줄이고 상수를 사용
#modifier function(비순수 함수): 함수의 실행이 외부 상태에 영향을 끼침, 변수 사용

def add(a,b):
    return a + b

print(add(1,2))

num_list = [1,2,3]

def append_num(n):
    num_list.append(n)

append_num(4)
print(num_list)
import random

#iter : 반복을 끝낼 값(sentinel)을 지정하면, sentinel이 나올 때 반복을 끝낸다
#iter(callable(호출 가능한 객체), sentinel) -> 따라서 callable에는 매개변수가 없는 함수 or lambda 넣어준다

for i in iter(lambda: random.randint(0,5),2):
    print(i, end=' ')


#next : 기본값을 지정할 수 있어, 반복이 끝나더라도 StopIteration 발생 대신 기본값이 출력됨 
#next(반복 가능한 객체, 기본값) -> 즉, 반복이 끝나면 기본값을 출력함

it = iter(range(3))
print(next(it,'end'))
print(next(it,'end'))
print(next(it,'end'))
print(next(it,'end'))   #위에서부터 0~2까지 출력 후, 'end' 출력

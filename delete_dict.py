#dict에서 요소 제거하기

x = {'a':1, 'b':2, 'c':3}

#pop
x.pop('a')
print(x)

#dict표현식 with if문 (for문으로 반복하면서 del을 사용하는 건 안됨 - RuntimeError: dictionary changed size during iteration)
x = { key:value for key,value in x.items() if key != 'a' }
print(x)
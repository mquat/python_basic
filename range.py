#range()도 list, tuple, 문자열 등 처럼 sequence object중 하나
#그러나 range()의 경우 연산 작용은 불가능하다 

x = range(0,3)
y = range(3,6)

#print(x+y) -> ERROR (unsupported types for range), range()는 iterator를 반환하는 것이지 list를 반환하는 것이 아님

print([*x, *y])     #unpacking을 사용해서 '+'연산자와 같이 붙일 수 있다
print([*x]*3)
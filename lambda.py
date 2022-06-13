#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

#lambda - basic examples
x = lambda a : a + 10
print(x(5))

y = lambda a, b, c : a + b + c
print(y(5,6,2))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
    return lambda a : a * n

result = myfunc(3)

print(result(11))

#함수의 인수 부분에서, 간단하게 함수를 만들기 위해서 - 대표적인 예시, map
#함수를 직접 만들어 map()에 넣을 수 있음 
#첫 번째 방법
def plus_ten(x):
    return x + 10

result = list(map(plus_ten, [1,2,3]))

#두 번째 방법 (lambda 함수 사용)
result = list(map(lambda x: x + 10, [1,2,3]))

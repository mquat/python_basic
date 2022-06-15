#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

#lambda - basic examples
from tabnanny import check


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

#-----------------------------------------------------------------
#아래와 같이 내부 콜백함수(어떤 이벤트가 발생했을 때 호출되는 함수)를 작성할 때 lambda 사용 
#그렇지 않으면 def func1, def func2, def func3 등처럼 함수를 따로 정의해야 한다 
Lambdas = [
    lambda x : x ** 2,
    lambda x : x ** 3,
    lambda x : x ** 4
]

for lambda_callback in Lambdas:
    print(lambda_callback(2))


#추가 연습문제 - lambda + if 조건문 
#lambda함수에서 if조건문은 1)무조건 else문이 있어야 하며, 2) 콜론을 붙이지 않는다 그리고 3)elif를 쓸 수 없다 
lambdas = [
    lambda x : 'SHORT_PASSWORD' if len(x) < 8 else None,
    lambda x : 'NO_CAPITAL_LETTER_PASSWORD' if not any(char.isupper() for char in x) else None
]

def check_password_using_lambda(password):
    for f in lambdas:
        if f(password) is not None:
            return f(password)

    return True

print(check_password_using_lambda('123'))
print(check_password_using_lambda('123456789f'))
print(check_password_using_lambda('123456789F'))
# is, ==
# is는 id값을 비교하는 연산자 
# ==은 값을 비교하는 연산자이기 때문에, None은 비교 불가능

import copy 


a = [1,2,3]

if a is None:
    pass

print(a == a)
print(a == list(a))
print(a is a)
print(a is list(a))     # list로 감싸면, 별도의 객체(즉, 별도의 id)에 생성된다 -> 결과는 false 

print(a == copy.deepcopy(a))    #true
print(a is copy.deepcopy(a))    #false
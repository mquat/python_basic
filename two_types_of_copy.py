#----------------------------------------------------
#shallow copy, deep copy
#mutable: list, set, dict
#immutable: int, float, str, bool, tuple, frozenset(set과 동일하나 immutable한 속성 가짐-요소 추가/삭제 불가능)

#set vs frozenset
a = frozenset({1,2,3})
a.update({5})
print(a)            #AttributeError: 'frozenset' object has no attribute 'update' (그냥 set이라면 결과는 {1,2,3,5})
#----------------------------------------------------

import copy
from copy import deepcopy

#----------------------------------------------------
#mutable - list / 원소가 변경되어도, id값이 동일함 
x = [1,2,3]
print(id(x))
x.append(5)
print(id(x))

#shallow copy
x = [1,2,3]
y = x               #shallow copy 
x[0] = 5            #따라서, y[0]도 5가 됨 
print(x,y)
print(id(x))    
print(id(y))


#----------------------------------------------------
#immutable - abc / 일부 글자 변경 불가능('str' object does not support item assignment) - 재할당 필요, 당연히 id값도 달라짐 
x = 'abc'
print(id(x))

x = 'abcd'
print(id(x))

#shallow copy
x = 'abc'
y = x 
y = 'zyx'
print(x,y)
print(id(x))
print(id(y))


#----------------------------------------------------
#shallow copy 

x = [[1,2],[3,4]]
y = copy.copy(x)        #y = x[:]와 같음 

x[1].append([5,6])
print(id(x))
print(id(y))

print(x==y)             #False, x 에 [5,6] 이 새로운 원소로 추가되면서 변경되었기 때문(다른 메모리 주소) 
print(x[1] is y[1])     #True, 즉 여전히 mutable 안에 mutable 한 객체는 같은 메모리 주소를 바라보고 있음 


#----------------------------------------------------
#deep copy - 내부 객체들까지 모두 새롭게 copy되는 것을 말함 
x = [[1,2],[3,4]]
y = copy.deepcopy(x)

x[1].append([5,6])
print(id(x))
print(id(y))

print(x==y)             #False
print(x[1] is y[1])     #False
#달팽이는 올라가고 싶다 

A,B,V = map(int,input().split())

# 결국 길이에 도달할지 말지는 A가 결정함 ... A-B+A-B... + A 에서 결정 
# (A-B)+A = V 

import math
result = math.ceil((V-A)/(A-B)+1)
print(result)
#손익분기점
from re import X


A,B,C = map(int,input().split())
#A는 고정비용, B는 가변비용/대 당, C는 가격/대 당 

if B >= C:
    print(-1)
else:
    print(int(A/(C-B)+1)) 

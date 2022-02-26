#기찍 n
#첫 번째 방법
from audioop import reverse


N = int(input())
for i in range(N):
    print(N)
    N -= 1 

#두 번째 방법: range(시작점, 종점, 스텝구간) 활용 
for i in range(int(input()),0,-1):
    print(i)

#A+B - 7

case = int(input())

for i in range(case):
    A,B = map(int,input().split())
    print("Case #{0}:" .format(i+1),end=" ")
    print(A+B)
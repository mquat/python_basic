#문자열 반복

T = int(input())

for t in range(T):
    R,S = input().split()
    for i in S: 
        print(int(R)*i, end= "")


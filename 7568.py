#덩치 순서 매기기: 일반적으로 생각하는 ranking이 아니라, 내 앞에 2명이 있으면 -> 3등과 같은 규칙을 생각해야 함.

def bigger(x,y):
    if (x[0] < y[0]) and (x[1] < y[1]):
        return True
    return False

N = int(input())

my_list = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    rank = 1
    for j in range(N):
        if bigger(my_list[i], my_list[j]):
            rank += 1
    
    print(rank, end=" ")
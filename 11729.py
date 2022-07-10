#하노이의 탑 

K = int(input())

def hanoi_move(num,a,b,c):
    #종료 조건
    if num == 1:
        print(a,c)
    else:
        hanoi_move(num-1,a,c,b)
        print(a,c)
        hanoi_move(num-1,b,a,c)

cnt = 0

for _ in range(K):
    cnt = (cnt*2) + 1

print(cnt)
hanoi_move(K,1,2,3) 
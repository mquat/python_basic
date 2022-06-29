#8*8로 자를 수 있는 모든 케이스마다 수정해야 하는 개수를 체크해야 함 
#그런데 수정해야 하는 개수를 세는 부분에서 로직을 생각하지 못했음 
#수정 개수: 각 칸의 좌표 기준으로 생각해야 함 ((0,0),(0,1)...) -> index끼리 합한게 홀수인 경우와 그렇지 않은 경우로 나눠서, White/Black 중 하나를 정해서 모두 통일시켜야 함 

N,M = map(int, input().split())

square= [input() for _ in range(N)]

fix_num = []

for n in range(N-7):
    for m in range(M-7):
        first_w = 0
        first_b = 0

        for i in range(n,n+8):
            for j in range(m,m+8):
                if (i+j)%2 ==0:
                    if square[i][j] != 'W' : first_w += 1
                    if square[i][j] != 'B' : first_b += 1
                else:
                    if square[i][j] != 'B' : first_w += 1 
                    if square[i][j] != 'W' : first_b += 1

        fix_num.append(first_w)
        fix_num.append(first_b)

print(min(fix_num))
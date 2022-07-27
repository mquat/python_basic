N = int(input())

#첫 번째 방법 - 이중 for문
for n in range(N,0,-1):
    print(' '*(N-n)+'*'*(2*n-1))
    if n == 1:
        for y in range(2,N+1):
            print(' '*(N-y)+'*'*(2*y-1))


#두 번째 방법 - 2개의 분리된 for문 
for n in range(N,1,-1):
    print(' '*(N-n)+'*'*(2*n-1))

for y in range(1,N+1):
    print(' '*(N-y)+'*'*(2*y-1))
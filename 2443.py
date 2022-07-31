N = int(input())

cnt = 1
for n in range(N,0,-1):
    print(' '*(N-n)+'*'*(2*N-cnt))
    cnt += 2 

    if n == 1:
        for y in range(2,N+1):
            print(' '*(N-y)+'*'*(2*y-1))
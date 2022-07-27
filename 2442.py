N = int(input())

#첫 번째 방법 
cnt = 1
for n in range(N,0,-1):
    print(' '*(n-1)+'*'*((2*cnt)-1))
    cnt += 1

#2번째 방법 
for n in range(1,N+1):
    print(' '*(N-n)+'*'*(2*n-1))
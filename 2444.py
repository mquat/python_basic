N = int(input())

for n in range(1,N):
    print(' '*(N-n)+'*'*(2*n-1))

for n in range(N,0,-1):
    print(' '*(N-n)+'*'*(2*n-1))
N = int(input())

for i in range(1, N+1):
    print('*'*i + ' '*2*(N-i) + '*'*i)

for k in range(1, N):
    print('*'*(N-k) + ' '*2*k + '*'*(N-k))
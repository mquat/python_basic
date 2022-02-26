#x보다 작은 수 
N,X = map(int,input().split())
A = list(map(int, input().split()))

#틀린 예시 - IndexError
for i in range(1,N+1):
    if A[i] < X:
        print(A[i], end=" ")

#옳은 예시
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")

#가변인자와 리스트 내포를 사용하면 좀 더 간결하게 만들 수 있다. (시간: 76ms)
N,X = map(int,input().split())
A = [*map(int,input().split())]
print(*[n for n in A if n < X])


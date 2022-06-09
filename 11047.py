#탐욕 알고리즘
#동전은 1,5,10,50,100,500,1000,5000...과 같이 주어짐. 즉, 상위 동전이 하위 동전의 배수라는 것이 point 

N, K = map(int, input().split())

#보통 list comprehension이 for문보다 빠른데, 아래의 경우 for문이 좀 더 빠르다
#아마도 직접 input()을 받는 것에서 원인이 있는 것 같은데, 좀 더 확인 필요함 
# coin = [int(input()) for _ in range(N)]
coin = []
for _ in range(N):
    coin.append(int(input()))

cnt = 0 

for i in reversed(range(N)):
    cnt += K//coin[i]
    K = K%coin[i]

print(cnt)
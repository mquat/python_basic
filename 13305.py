#첫째줄 - 도시의 개수, N
#둘째줄 - 인접 두 도시를 연결하는 도로의 길이
#셋째줄 - 주요소의 리터당 가격 (제일 왼쪽 도시부터)

N = int(input())

distance = list(map(int, input().split()))
price = list(map(int, input().split()))

#처음에는 무조건 첫 번째 가격을 내야 한다 (price[0])
start_price = price[0]
total_price = price[0] * distance[0]

#price[1], distance[1]부터 시작: 만약 start_price가 price[1]보다 싸면, start_price * distance[1]을 해서 더하면 최소 비용
for i in range(1,N-1):
    if start_price > price[i]:
        start_price = price[i]

    total_price += start_price * distance[i]    
        
print(total_price)
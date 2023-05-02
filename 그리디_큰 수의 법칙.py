n, m, k = map(int, input().split())
array_n = list(map(int, input().split()))

array_n.sort(reverse=True)
first = array_n[0]
second = array_n[1]

result = 0

##첫 번째 방법
while True:
    for i in range(k):  #최대 k번까지 first를 더할 수 있고, 그 다음에는 second로 넘어간다
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1


##두 번째 방법
count = int(m/(k+1)) * k    #반복하는 수열의 길이는 k+1 -> (전체 길이/반복 수열의 길이)의 몫 * k 는 first의 총 개수
count += m % (k+1)          #(전체 길이/반복 수열의 길이)의 나머지가 0이 아닌 경우, 나머지만큼 first를 더해줘야 함

result = 0
result += (count) * first   
result += (m-count) * second    #(m-count) = second의 개수

print(result)


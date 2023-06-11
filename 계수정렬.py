#계수정렬은 특정 조건(데이터 크기가 제한되고 정수 형태로 표현)에서만 유리하게 사용할 수 있다

array = [7, 5, 9, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

#가장 작은 수가 0이고 가장 큰 수가 9이므로, 원소가 10개인 별도의 list를 만들면 됨
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    #각 원소 별로 개수만큼 print한다
    for j in range(count[i]):
        print(i, end=' ')


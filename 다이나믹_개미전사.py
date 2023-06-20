n = int(input())

array = list(map(int, input().split()))

result = [0] * 100

result[0] = array[0]
result[1] = max(array[0], array[1])
for i in range(2, n):
    result[i] = max(result[i-1], result[i-2] + array[i])

print(result[n-1])


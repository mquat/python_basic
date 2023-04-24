N,M = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total_length = 0
    mid = (start+end)//2
    for x in array:
        if x > mid:
            total_length += (x-mid)
    
    if total_length < M:
        end = mid-1
    else:
        result = mid
        start = mid+1


print(result)


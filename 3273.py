N = int(input())
num_list = list(map(int, input().split()))
x = int(input())

num_list.sort()
cnt = 0 
start = 0
end = N-1

while start < end:
    two_sum = num_list[start] + num_list[end]
    if two_sum == x:
        cnt += 1
    if two_sum < x:
        start += 1
        continue 
    end -= 1

print(cnt)
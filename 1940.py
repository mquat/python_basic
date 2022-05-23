N = int(input())
M = int(input())
my_list = list(map(int, input().split()))

#시간초과 
# length = len(my_list)
# cnt = 0

# for i in range(0, length-1):
#     for j in range(i+1, length):
#         result = my_list[i] + my_list[j]
#         if result != M: continue
#         cnt += 1 

# print(cnt)


#투포인터
my_list.sort()
start, end = 0, len(my_list)-1
cnt = 0 
while start < end: 
    result = my_list[start] + my_list[end]
    if result > M:
        end -= 1 
    elif result < M:
        start += 1
    else:
        cnt += 1 
        start += 1 
        end -= 1 

print(cnt)
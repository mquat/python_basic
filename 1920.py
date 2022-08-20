
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))



#첫 번째 방법 - 시간 초과
# for i in B:
#     print(1) if i in A else print(0)


#두 번째 방법 - 이분 탐색
def binary_search(target,data):
    data.sort()
    start = 0
    end = len(data) -1

    while start <= end:
        mid = (start + end)//2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid-1

for target in B:
    idx = binary_search(target,A)
    if idx:
        print(1)
    else:
        print(0)

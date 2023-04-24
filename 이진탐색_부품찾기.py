#이진탐색 
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

#부품의 개수
N = int(input())
array_n = list(set(map(int,input().split())))
M = int(input())
array_m = list(set(map(int, input().split())))

#오름차순 정렬
array_n.sort()
array_m.sort()

for i in array_m:
    if binary_search(array_n, i, 0, N):
        print('yes', end= ' ')
    else:
        print('no', end=' ')


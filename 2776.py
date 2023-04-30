def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return 0

T = int(input())

for _ in range(T):
    N = int(input())
    array_n = list(map(int, input().split()))
    M = int(input())
    array_m = list(map(int, input().split()))

    array_n.sort()

    for i in array_m:
        print(binary_search(array_n, i, 0, N-1))


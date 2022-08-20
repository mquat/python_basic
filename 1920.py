N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))



#첫 번째 방법 - 시간 초과
# for i in B:
#     print(1) if i in A else print(0)


#두 번째 방법 - 이분 탐색
#만약 이분탐색을 binary_search()라는 함수로 따로 정의하고, for문을 통해 B의 요소를 하나씩 꺼내서 함수 적용하면 이것도 시간초과! 
A.sort()

for target in B:
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end)//2

        if A[mid] == target:
            print(1)
            break
        elif A[mid] < target:
            start = mid+1
        else:
            end = mid-1
        
    if target not in A:
        print(0)
#재귀를 이용한 이진탐색 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    #만약 target과 같으면 index값 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


#n은 원소의 개수, target은 찾고자 하는 문자열
n, target = list(map(int, input().split()))

#전체 원소 입력
array = list(map(int, input().split()))

#결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)


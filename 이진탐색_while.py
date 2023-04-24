#while문을 통한 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        #중간값이 target보다 크다면 end 지점을 mid-1로 옮긴다
        elif array[mid] > target:
            end = mid-1
        #중간값이 target보다 작다면 start지점을 mid+1로 옮긴다
        else:
            start = mid+1
    return None


#전체 원소 입력받기
array = list(map(int, input().split()))

#n은 원소의 개수, target은 찾고자 하는 문자열
n, target = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)


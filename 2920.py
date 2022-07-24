
new_scale = list(map(int,input().split()))

## 첫 번째 방법 - 2가지 버전의 scale 리스트를 만들고, 비교하기 
scale = [1,2,3,4,5,6,7,8]
scale_reversed = [8,7,6,5,4,3,2,1]

if new_scale == scale:
    print("ascending")
elif new_scale == scale_reversed:
    print("descending")
else:
    print("mixed")


##두 번째 방법 - sorted 사용
if new_scale == sorted(new_scale):
    print("ascending")
elif new_scale == sorted(new_scale,reverse=True):
    print("descending")
else:
    print("mixed")


##sort - sort는 새 목록을 반환하지 않고 동일한 목록을 정렬시킴, 따라서 new_scale.sort() 자체는 None을 반환함 - 따라서 어떤 case든 mixed를 반환함 
if new_scale == new_scale.sort():
    print("ascending")
elif new_scale == new_scale.sort(reverse=True):
    print("descending")
else:
    print("mixed")

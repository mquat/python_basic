from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()     #투포인터 실행을 위해 먼저 정렬한다

    for i in range(len(nums)-2):
        #기준값 nums[i]를 중심으로, 같은 값이 나오면 다음 인덱스로 넘어간다
        if i > 0 and nums[i] == nums[i-1]:
            continue

        #나머지 요소에서 투포인터 적용
        left, right = i+1, len(nums)-1
        while left < right:
            target = nums[i] + nums[left] + nums[right]
            
            if target < 0:
                left += 1
            elif target >0:
                right -= 1
            else:
                #원하는 결과(세 수의 총합=0)이므로, result에 list로 묶어 더해준다
                results.append([nums[i], nums[left], nums[right]])
            
                #정답 처리 후, left/right 각각 양 옆으로 동일한 값이 있을 수 있으므로 이를 먼저 처리한다
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1

    return results


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
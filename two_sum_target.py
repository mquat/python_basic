from typing import List

#덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴해라

def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    #결과를 dict의 key로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [i,nums_map[target-num]]

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))

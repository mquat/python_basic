from typing import List

nums = [1,4,3,2]

def arrayPairSum(nums:List[int]) -> int:
    nums.sort()
    pair = []
    result = 0

    for num in nums:
        pair.append(num)
        if len(pair) == 2:
            result += min(pair)
            #pair 초기화
            pair = []

    return result

print(arrayPairSum(nums))


##더 간결한 방법 (min(i,j)에서 어차피 min은 j이다!)
def arrayPairSum2(nums:List[int]) -> int:
    nums.sort()
    result = 0

    for i,n in enumerate(nums):
        if i%2 == 0:
            result += n

    return result

print(arrayPairSum2(nums))


##더더 간결한 방법
def arrayPairSum3(nums:List[int]) -> int:
    return sum(sorted(nums)[::2])

print(arrayPairSum3(nums))
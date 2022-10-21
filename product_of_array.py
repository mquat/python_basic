from typing import List

#O(n)으로 제한. 아래의 풀이 방법은 O(2n)이므로, 결국 O(n)이다 
def productExceptSelf(nums:List[int])-> List[int]:
    result = []
    p = 1   #보통 count할 때 설정하는 초기값(cnt=0)과 같은 개념. 여기서는 곱하기이므로 1로 설정한다 
    
    #해당 숫자를 기준으로 왼쪽에 있는 값들만 순차적으로 곱한다
    for i in range(0,len(nums)):
        result.append(p)
        p *= nums[i]    #left의 결과는 [1,1*1,1*2,1*2*3]

    #해당 숫자를 기준으로 오른쪽에 있는 값들만 순차적으로 곱한다 
    p = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= p  
        p *= nums[i]    #right의 결과는 [1*4*3*2,1*4*3,2*4,6*1]

    return result


nums = [1,2,3,4]
print(productExceptSelf(nums))
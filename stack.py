
#stack을 이용해 문제 풀기
#주어진 문자열에서, 중복된 문자를 없애고 만들 수 있는 순서 상 가장 빠른(사전 기준) 단어 조합 만들기
from collections import Counter

lst = 'cbacdcbc'
new_dict = Counter(lst)

stack = []

for char in lst:
    new_dict[char] -= 1

    if not stack:
        stack.append(char)
    elif char in stack:
        pass
    else:
        while stack and stack[-1] > char and new_dict[stack[-1]] != 0:
            stack.pop()
        
        stack.append(char)

    
result = ''.join(stack)
print(result)
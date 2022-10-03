
def longestPalindrome(s: str)-> str:
    def expand(left: int, right:int) -> str:
        #palindrome이라면,양 옆으로 1씩 더 확장하여 palindrome인지 추가 확인한다 
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s)-1):
        #2가지 case: 중간에 1글자 짜리 palindrome이 있는 경우와 아닌 경우
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        print(result)      

    return result

s = 'cbbd'
print(longestPalindrome(s))
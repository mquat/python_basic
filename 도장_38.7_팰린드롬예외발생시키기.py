class notPalindromeError(Exception):
    def __init__(self):
        print('회문이 아닙니다.')

def palindrome(word):
    if word != word[::-1]:
        raise notPalindromeError
    print(word)
    

try:
    word = input()
    palindrome(word)
except notPalindromeError as e:
    print(e)


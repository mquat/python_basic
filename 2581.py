#1978 소수 문제에서 정의한 소수 판별 함수와 동일 
def prime_num(number):
    if number == 1:
        return False
    for i in range(2,int((number**(1/2)))+1):
        if number%i == 0:
            return False
    return True

N = int(input())
M = int(input())

#range안 숫자를 하나씩 검사, 소수면(True) lst에 append
lst = [i for i in range(N, M+1) if prime_num(i) == True]

if not lst:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))
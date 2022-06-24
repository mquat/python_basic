def isPrime(num):
    if num == 1: return False
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0: return False
    return True

while True:
    N = int(input())
    
    #마지막 test case는 항상 0이다. 때문에, while문 안에서 if N==0이면 while문을 break하고 종료하는 코드를 작성 (or 런타임에러)
    if N == 0: break
    cnt = 0

    for i in range(N+1, (2*N)+1): 
        if isPrime(i): cnt += 1

    print(cnt)

N = int(input())
X = list(map(int, input().split()))

##1번째 방법 
result = []
for x in list(X):
    if x == 1: 
        pass
    else:
        for i in range(2,x):
            if x%i == 0:
                break
        else:
            result.append(x)

print(len(result))


##2번째 방법 
def is_prime(n):
    if n == 1:
        return False
    
    #1/2제곱근을 하는 이유는, 절반만 체크하면 되기 때문. 
    #추가로 1을 더하는데, 2를 더하면 오류가 남 (반례: 2, range(2,2)가 되고 for문 실행 못하고 True를 반환해버림)
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            return False

    return True

cnt = 0 
for x in X:
    if is_prime(x): cnt += 1 

print(cnt)
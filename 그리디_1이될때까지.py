n, k = map(int, input().split())
cnt = 0


##방법1
while n >= k:
    while n % k != 0:
        n -= 1
        cnt += 1
    n //= k
    cnt += 1

#아래 과정을 해주지 않으면, 예를 들어 n=25, k=3 이면 cnt=6이어야 하는데 cnt=5가 된다
while n > 1:
    n -= 1
    cnt += 1


##방법2
while True:
    target = (n//k)*k

    cnt += (n-target)
    n = target

    if n < k:
        break

    cnt += 1
    n //= k

cnt += (n-1)
print(cnt)


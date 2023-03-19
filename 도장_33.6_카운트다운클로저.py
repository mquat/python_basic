def countdown(n):
    n = n+1
    def wrapper():
        nonlocal n
        n -= 1
        return n
    return wrapper


n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')
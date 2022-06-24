def is_prime(num):
    if num ==1: return False
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    num = int(input())
    a = num//2
    b = num//2

    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        else:
            a -= 1
            b += 1 
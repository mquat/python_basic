#팩토리얼

def solve(x):
    result = 1
    if x>0:
        result = x*solve(x-1)
    return result

x = int(input())
print(solve(x))
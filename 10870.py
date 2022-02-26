#피보나치 수 5

def solve(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    return solve(x-1)+solve(x-2)

x = int(input())
print(solve(x))


# n = int(input())
# num = []
# for x in range(n):
#     if x == 0 or x ==1: num.append(1)
#     else:
#         fibo_num = num[-1]+num[-2]
#         num.append(fibo_num)

# print(num[n-1])
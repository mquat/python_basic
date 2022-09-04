n = int(input())

number_list = [0,1]

# for i in range(2, n+1):
#     number_list.append(number_list[-2]+number_list[-1])

# print(number_list[n])

#다른 접근 
def fibonacci(num):
    if n == 0:
        return 0
    elif n== 1 or n == 2:
        return 1
    else:
        while len(number_list) <= num:
            number_list.append(number_list[-2]+number_list[-1])
        return number_list[-1]

print(fibonacci(n))
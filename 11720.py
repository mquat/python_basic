#숫자의 합
# N = int(input())
# C = int(input())

# new_C = list(str(C))
# result = 0
# for i in new_C:
#     num = int(i)
#     result += num

# print(result)


N = int(input())
C = list(input())

result = 0
for x in C:
    result += int(x)

print(result)
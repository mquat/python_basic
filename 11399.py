N = int(input())
M = list(map(int, input().split()))

M.sort()
result = 0 

#첫 번째 방법 (116ms)
# for i in range(0,len(M)):
#     for j in range(i+1):
#         result += M[j]

# print(result)


#두 번째 방법 (112ms)
for i in range(0,len(M)):
    result += M[i] * (len(M)-i)

print(result)
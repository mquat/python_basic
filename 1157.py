#단어 공부
answer = input().upper()

A = list(answer)
B = list(set(A))
cnt = []
#num = []

#첫 번째 방법 - 0.4초 
for i in B:
    count = A.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >=2:
    print("?")
else:
    print(B[cnt.index(max(cnt))])

#두 번째 방법 - 2초
# for i in B:
#     cnt = 0
#     for j in A:
#         if i == j:
#             cnt += 1 
#     num.append(cnt)

# if num.count(max(num)) >=2:
#     print("?")
# else:
#     print(B[num.index(max(num))])
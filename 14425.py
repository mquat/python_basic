from collections import defaultdict

N, M = map(int, input().split())

#구현은 됐으나 시간초과(list 사용)
# S = [input() for i in range(N)]
# X = [input() for i in range(M)]

# cnt = 0 
# for word in S:
#     cnt += X.count(word)

# print(cnt)


#통과(dict 사용)
S = defaultdict(int)
for i in range(N):
    S[input()] = 1

X = [input() for i in range(M)]
cnt = 0

for word in X:
    if S[word]: cnt += 1

print(cnt)
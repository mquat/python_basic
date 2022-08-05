N,M = map(int,input().split())

s1 = {input() for _ in range(N)}
s2 = {input() for _ in range(M)}

result_set = s1 & s2
result_set = list(result_set)
result_set.sort()

print(len(result_set))
for member in result_set: print(member)
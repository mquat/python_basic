N = int(input())
lst = [int(input()) for _ in range(N)]
new_lst = []

for x in lst:
    if x ==0 :
        new_lst.pop()
    else:
        new_lst.append(x)

print(sum(new_lst))
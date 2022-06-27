N= int(input())

result = 0

for constr in range(N):
    max_total = sum(list(map(int, str(constr))))

    if(constr + max_total == N):
        result = constr
        break 

print(result)

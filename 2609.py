n,m = map(int, input().split())

std_num = min(n,m)

for i in range(std_num,0,-1):
    value1 = n%i
    value2 = m%i

    if value1 == 0 and value2 == 0:
        print(i)
        print(i*(n//i)*(m//i))
        break
    else:
        continue    
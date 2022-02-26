#셀프 넘버


def con_num(n):
    if n<100:
        return n+(n//10)+(n%10)
    elif n<1000:
        return n+(n//100)+((n%100)//10)+((n%100%10))
    elif n<10000:
        return n+(n//1000)+((n%1000)//100)+((n%1000%100)//10)+((n%1000%100)%10)

total_num = set(list(range(1,10001)))
self_num = set([con_num(x) for x in range(1,10001)])

result = sorted(total_num - self_num)

for answer in result:
    print(answer)




N = int(input())

order_list = []
for _ in range(N):
    order = tuple(map(str, input().split()))
    order_list.append(order)

result = [] 
for order in order_list:
    if order[0] == 'push':
        result.append(int(order[1]))

    elif order[0] == 'pop':
        if result: 
            print(int(result.pop()))
        else:
            print(-1)

    elif order[0] == 'size': 
        print(len(result))

    elif order[0] == 'empty':
        if result:
            print(0)
        else:
            print(1)

    elif order[0] == 'top':
        if result:
            print(result[-1])
        else:
            print(-1)
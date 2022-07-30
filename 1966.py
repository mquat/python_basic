case = int(input())

for _ in range(case):
    N,M = map(int,input().split())
    priority = list(map(int,input().split()))
    check_priority = [i for i in range(N)]
    check_priority[M] = 'target'
    order = 0

    while priority:
        if priority[0] == max(priority):
            order += 1
            if check_priority[0] == 'target':
                print(order)
                break
            priority.pop(0)
            check_priority.pop(0)
        else:
            priority.append(priority.pop(0))
            check_priority.append(check_priority.pop(0))

#비트마스크: 각 자리의 bit를 이용해 bool형 list를 만드는 것, 메모리를 절약할 수 있음
import sys 

M = int(sys.stdin.readline())
S = 0 

for _ in range(M):
    operator = sys.stdin.readline().rstrip().split()

    if operator[0] == 'all':
        S = (1 << 20) -1

    elif operator[0] == 'empty':
        S = 0

    elif operator[0] == 'add':
        S |= (1 << int(operator[1])-1)

    elif operator == 'remove':
        S &= ~(1 << int(operator[1])-1)

    elif operator == 'check':
        print(1) if S & (1 << int(operator[1])-1) == 0 else print(0)

    elif operator == 'toggle':
        S ^= (1 << int(operator[1])-1)


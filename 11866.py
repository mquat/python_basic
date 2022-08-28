from collections import deque

N, K = map(int, input().split())

circle = deque()
for i in range(1,N+1):
    circle.append(i)

print('<',end='')
while circle:
    for _ in range(K-1):
        circle.append(circle.popleft())
    print(circle.popleft(), end='')
    if circle:
        print(', ', end='')
print('>')

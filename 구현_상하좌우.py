n = int(input())
x,y = 1,1
steps = input().split()

type = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for step in steps:
    for i in range(len(type)):
        if step == type[i]:
            sx = x + dx[i]
            sy = y + dy[i]
    #전체 map을 무시하면 해당 명령어는 무시하고 다음으로 넘어간다
    if sx < 1 or sy <1 or sx > n or sy > n:
        continue
    
    x,y = sx, sy

print(x,y)



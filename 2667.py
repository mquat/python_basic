from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(h,w):
    queue = deque()

    queue.append([h,w])
    visited[h][w] = 1
    result = 1

    while queue:
        h,w = queue.popleft()

        for i in range(4):
            hh = h + dy[i]
            ww = w + dx[i]

            if hh < 0 or hh >= N or ww < 0 or ww >= N:
                continue
            
            if graph[hh][ww] == 1 and visited[hh][ww] == 0:
                queue.append([hh,ww])
                visited[hh][ww] = 1
                result += 1 

    house.append(result)

N = int(input())

graph = []
for _ in range(N):
    graph.append([int(i) for i in input()])

visited = [[0]*N for _ in range(N)]

house = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j)


house.sort()

print(len(house))
for cnt in house:
    print(cnt)


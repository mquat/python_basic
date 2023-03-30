from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(h,w):
    queue = deque()

    queue.append([h,w])
    visited[h][w] = 1

    while queue:
        h,w = queue.popleft()

        for i in range(4):
            hh = h + dy[i]
            ww = w + dx[i]

            if ww < 0 or ww >= M or hh < 0 or hh >= N:
                continue

            if graph[hh][ww] and visited[hh][ww] == 0:
                queue.append([hh,ww])
                visited[hh][ww] = 1
                

T = int(input())

for _ in range(T):
    M,N,K = map(int, input().split())

    graph = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    for _ in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1

    result = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] and visited[i][j] == 0:
                result += 1
                bfs(i,j)

    print(result)
from collections import deque

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]

def bfs(h,w):
    queue = deque()

    queue.append([h,w])

    while queue:
        h,w = queue.popleft()

        for i in range(8):
            hh = h + dy[i]
            ww = w + dx[i]
            
            if hh < 0 or hh >= M or ww < 0 or ww >= N:
                continue

            if graph[hh][ww] == 1:
                queue.append([hh,ww])
                graph[hh][ww] = 0

            if graph[hh][ww] == 0:
                continue
                



while True:
    N,M = map(int, input().split())
    
    if N == 0 and M == 0:
        break
    
    graph = []
    for _ in range(M):
        graph.append(list(map(int, input().split())))

    total_land = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                total_land += 1
                bfs(i,j)       

    print(total_land)
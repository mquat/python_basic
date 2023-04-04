import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

N,M,R = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(N+1)]
visited = [0] * (N+1)
count = 1 

def dfs(v):
    global count
    visited[v] = count
    graph[v].sort()

    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(i)

dfs(R)

for i in range(1, N+1):
    print(visited[i])


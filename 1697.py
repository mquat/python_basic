from collections import deque

N,K = map(int,input().split())

max = 10**5
visited = [0]*(max+1)

def bfs():
    queue = deque()
    queue.append([N,0])

    while queue:
        pos, cnt = queue.popleft()
        #K(최종 지점)에 도달하면 멈추고 cnt 출력
        if pos == K:
            print(cnt)
            break

        dx = [pos-1, pos+1, pos*2]

        for i in dx:
            if 0 <= i <= max and not visited[i]:
                visited[i] = visited[pos] + 1
                queue.append([i,visited[i]])


bfs()


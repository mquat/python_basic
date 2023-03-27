def dfs_example(graph, v, visited):
    visited[v] = True   #방문한 경우, True로 변경
    print(v, end=' ')

    #현재 노드와 연결된 다른 노드를 탐색한다
    # node1과 연결된 노드들을 가지고 for문 -> 재귀함수를 통해, 연결된 노드를 순차적으로 스택에 넣기(방문한 경우 탐색 중단)
    for i in graph[v]:
        if not visited[i]:
            dfs_example(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#DFS 탐색 전 모든 값의 visited 정보는 False
visited = [False] * 9

dfs_example(graph, 1, visited)
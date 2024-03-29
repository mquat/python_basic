#인접행렬: 각 노드(index)를 기준으로, 모든 관계 정보(다른 노드(각 요소 안의 index), 거리)를 표시한다 (=2차원 배열)
INF = 9999999999

graph1 = [
    [0,7,5],    #예를 들어, 노드0과 노드1의 거리는 7임
    [7,0,INF],  #노드1과 노드0의 거리는 마찬가지로 7임
    [5,INF,0]
]

print(graph1)


#인접리스트: 각 노드(index)를 기준으로, 연결 정보(다른 노드, 거리)만 표시한다 
graph2 = [[] for _ in range(3)]

graph2[0].append((1,7))    #예를 들어, 노드0과 노드1의 거리는 7임
graph2[0].append((2,5))    #노드0과 노드2의 거리는 5임

graph2[1].append((0,7))
graph2[2].append((0,5))

print(graph2)
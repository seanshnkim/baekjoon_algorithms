# 2022-07-13, Sehyun Kim
import sys
from collections import deque

# BFS를 통해 특정 노드(1개)와 연결되어 있는 모든 노드의 개수를 찾는 방식
# count하는 함수 필요
nNode = int(input())
nEdge = int(input())

# graph2DArr[0] = []
graph2DArr = [[] for _ in range(nNode+1)]

for _ in range(nEdge):
    s, e = map(int, sys.stdin.readline().split())
    graph2DArr[s].append(e)
    graph2DArr[e].append(s)

visited = [False] * (nNode + 1)

def bfs(graph, visited, start):
    cnt = 0
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        cnt += 1

        for adjNode in graph[v]:
            if not visited[adjNode]:
                queue.append(adjNode)
                visited[adjNode] = True
    # exclude 1(start node) itself
    return cnt-1 

print(bfs(graph2DArr, visited, 1))

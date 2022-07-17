# 2022-07-06, Sehyun Kim
from collections import deque

def dfs(graph, v, unvisited):
    if v not in unvisited:
        return 0
    else:
        unvisited.remove(v)
        print(v, end=' ')

        for i in graph[v]:
            if i in unvisited:
                dfs(graph, i, unvisited)


def bfs(graph, start, unvisited):
    queue = deque([start])

    unvisited.remove(start)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if i in unvisited:
                queue.append(i)
                unvisited.remove(i)


nNode, nEdge, start = map(int, input().split())

graph = {}
unvisited = set([])

for nE in range(nEdge):
    s, e = map(int, input().split())
    unvisited.update([s,e])

    if s in graph:
        graph[s].append(e)
    else:
        graph[s] = [e]
    if e in graph:
        graph[e].append(s)
    else:
        graph[e] = [s]

for v in graph.values():
    v.sort()

# visited = [False] * nNode

# unvisited를 sort할 필요 없다.
unvisited_cp = unvisited.copy()
node = start

# if it is an isolated vertex
# isolated vertex can be only reached if and only if it is set to start vertex
if start not in graph:
    print(start, start, sep='\n')
else:
    while unvisited:
        dfs(graph, node, unvisited)
        if unvisited:
            node = unvisited[0]

    print()
    bfs(graph, start, unvisited_cp)



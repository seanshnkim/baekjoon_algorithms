import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
in_degree = [0]*(N+1)
q = deque()
answer = []

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    in_degree[e] += 1

for adj_node in range(1, N+1):
    if in_degree[adj_node] == 0:
        q.append(adj_node)

while q:
    cur_node = q.popleft()
    answer.append(cur_node)
    
    for adj_node in graph[cur_node]:
        in_degree[adj_node] -= 1
        if in_degree[adj_node] == 0:
            q.append(adj_node)

print(*answer)
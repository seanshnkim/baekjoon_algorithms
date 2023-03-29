import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline
import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))


def dijkstra(start, dest):
    dist = [float('inf')]*(N+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (dist[start], start))
    
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        
        for adj_w, adj_node in graph[cur_node]:
            next_dist = cur_dist + adj_w
            
            if dist[adj_node] > next_dist:
                dist[adj_node] = next_dist
                heapq.heappush(q, ( next_dist, adj_node ) )
    
    return dist[dest]


# 각 1~N번 노드에 대해 X번까지의 최장 경로를 구하고, 다시 X번부터 1~N번까지의 최장 경로를 구한다.
# k번 노드 ~ X번 노드 최장 경로 + X번 노드 ~ k번 노드 최장 경로 합이 가장 큰 경우를 출력한다.
k2X = []
X2k = []
for start in range(1, N+1):
    k2X.append(dijkstra(start, X))
    X2k.append(dijkstra(X, start))

answer = 0
for dA, dB in zip(k2X, X2k):
    if answer < dA + dB:
        answer = dA + dB
print(answer)
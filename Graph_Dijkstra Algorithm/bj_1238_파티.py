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


def dijkstra_longest(start, dest):
    # 최장 경로를 구하는 것이기 때문에 float('inf')가 아니라 0으로 초기화해준다.
    dist = [0]*(N+1)
    # dist[start] = 0 -> 어차피 0으로 모두 초기화했기 때문에 이 코드는 필요 X
    q = []
    heapq.heappush(q, (dist[start], start))
    
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        cur_dist *= -1
        
        # 최단 경로를 구할 땐 어차피 한번 목적지에 도달하면
        # 경로 가중치 합이 늘어나기만 하기 때문에 더 이상 알아서 탐색을 수행하지 않지만,
        # 여기선 최장 경로를 구하고 있으므로 한번 이상 목적지(dest)에 도달해도
        # greedy algorithm 원리에 따라 이웃 노드를 계속 탐색할 수 있다. 따라서 이걸 방지해야 함
        if cur_node == dest:
            continue
        
        for adj_w, adj_node in graph[cur_node]:
            next_dist = cur_dist + adj_w
            # 최단 경로가 아니라 최장 경로를 구하는 과정임을 명심
            if dist[adj_node] < next_dist:
                dist[adj_node] = next_dist
                heapq.heappush(q, ( (-1)*next_dist, adj_node ) )
    
    return dist[dest]


# 각 1~N번 노드에 대해 X번까지의 최장 경로를 구하고, 다시 X번부터 1~N번까지의 최장 경로를 구한다.
# k번 노드 ~ X번 노드 최장 경로 + X번 노드 ~ k번 노드 최장 경로 합이 가장 큰 경우를 출력한다.
k2X = []
X2k = []
for start in range(1, N+1):
    k2X.append(dijkstra_longest(start, X))
    X2k.appennd(dijkstra_longest(X, start))

answer = 0
for dA, dB in zip(k2X, X2k):
    if answer > dA + dB:
        answer = dA + dB
print(answer)
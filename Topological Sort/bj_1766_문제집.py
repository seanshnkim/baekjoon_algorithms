import sys
import heapq
input = sys.stdin.readline

N, num_pair = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0]*(N+1)
q = []
ans_order = []

for _ in range(num_pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

# q에 우선 root node(in_degree 값이 0인 노드)를 대입한다.

for i in range(1, N+1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)

# root node부터 탐색 시작.
while q:
    cur_node = heapq.heappop(q)
    ans_order.append(cur_node)
    
    for adj_node in graph[cur_node]:
        in_degree[adj_node] -= 1
        if in_degree[adj_node] == 0:
            heapq.heappush(q, adj_node)

print(' '.join(map(str, ans_order)))
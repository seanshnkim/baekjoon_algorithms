import sys
input = sys.stdin.readline
import heapq

N = int(input())
graph = [[] for _ in range(N+1)]
in_degree = [0]*(N+1)
times = [0]*(N+1)

for i in range(1, N+1):
    inputs = list(map(int, input().split()))
    times[i] = inputs[0]
    
    num_prev = inputs[1]
    in_degree[i] += num_prev
    for k in range(2, 2+num_prev):
        graph[inputs[k]].append(i)

root_nodes = []
for i in range(1, N+1):
    if in_degree[i] == 0:
        # root_nodes.append( (-times[i], i) )
        heapq.heappush(root_nodes, (times[i], i) )


dp = [0]*(N+1)

while root_nodes:
    t, cur_root = heapq.heappop(root_nodes)
    dp[cur_root] += t
    
    for adj_node in graph[cur_root]:
        in_degree[adj_node] -= 1
        if in_degree[adj_node] == 0:
            heapq.heappush(root_nodes, ( (times[adj_node]+dp[cur_root]), adj_node) )

print(max(dp))
import sys
import heapq
input = sys.stdin.readline

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


round_trip_dist = []
for start in range(1, N+1):
    round_trip_dist.append( dijkstra(start, X) + dijkstra(X, start) )

print(max(round_trip_dist))
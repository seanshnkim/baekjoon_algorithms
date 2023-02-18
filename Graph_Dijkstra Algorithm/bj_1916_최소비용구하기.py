import sys
from collections import namedtuple
Edge = namedtuple("Edge", ["node", "weight"])
import heapq

V = int(input())
E = int(input())

adj_list = [[] for _ in range(V+1)]
for _ in range(E):
    start, end, w = map(int, input().split())
    adj_list[start].append(Edge(node=end, weight=w))

targ, dest = map(int, input().split())


def dijkstra(adj_list, start):
    # dist = {node: float('inf') for node in adj_list}
    dist = [float('inf') for _ in range(V+1)]
    dist[start] = 0
    
    pq = [start]
    visited = set()
    
    while pq:
        curr_node = heapq.heappop(pq)
        
        if curr_node in visited:
            continue

        visited.add(curr_node)
        
        for adj_node, w in adj_list[curr_node]:
            new_dist = dist[curr_node] + w
            if new_dist < dist[adj_node]:
                dist[adj_node] = new_dist
                heapq.heappush(pq, adj_node)
    
    return dist

dist_info = dijkstra(adj_list, targ)
print(dist_info[dest])
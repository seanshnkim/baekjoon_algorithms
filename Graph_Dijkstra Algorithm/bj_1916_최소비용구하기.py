import sys
input = sys.stdin.readline
import heapq

V = int(input())
E = int(input())

adj_list = [[] for _ in range(V+1)]
for _ in range(E):
    start, end, w = map(int, input().split())
    adj_list[start].append((end, w))

targ, dest = map(int, input().split())

# 먼저 삽입된 더 먼 경로의 정점은 탐색을 시작하지 않아야 합니다
# https://www.acmicpc.net/board/view/71228
# for i in range(1, V+1):
#     tmp_adj_nodes = {}
#     for e in adj_list[i]:
#         if e.node not in tmp_adj_nodes:
#             tmp_adj_nodes[e.node] = e.weight
#         else:
#             if e.weight < tmp_adj_nodes[e.node]:
#                 tmp_adj_nodes[e.node] = e.weight
#     adj_list[i] = [Edge(node=n, weight=w) for n,w in tmp_adj_nodes.items()]


def dijkstra(adj_list, start):
    # dist = {node: float('inf') for node in adj_list}
    dist = [float('inf') for _ in range(V+1)]
    dist[start] = 0
    
    pq = [(0, start)]
    visited = [False for _ in range(V+1)]
    
    while pq:
        d, curr_node = heapq.heappop(pq)
        
        if visited[curr_node] or dist[curr_node] < d:
            continue
        
        visited[curr_node] = True
        
        for adj_node, w in adj_list[curr_node]:
            new_dist = dist[curr_node] + w
            
            if new_dist < dist[adj_node]:
                dist[adj_node] = new_dist
                #FIXME - 온갖 걸 다시 검토하게 된다. 좋다.
                # 개념 부실하게 이해하던 것보단 훨씬 낫다. 여기에 visited[] = True 들어가면 안됨.
                # visited[adj_node] = True
                #FIXME - 
                # heappush -> 넣을 때 (weight, node) 순서로 push 하는 이유가 다 있다.
                # 0번째 원소를 기준으로 정렬하기 때문.
                # FIXME - w를 삽입하는 게 아니라, new_distance를
                # heapq.heappush(pq, (w, adj_node) )
    
    return dist

dist_info = dijkstra(adj_list, targ)
print(dist_info[dest])
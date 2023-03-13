import sys
input = sys.stdin.readline
import heapq


def dijkstra(start, end):
    hq = [(0, start)]
    dist = [float('inf')]*(V+1)
    dist[start] = 0
    
    while hq:
        cur_dist, cur_node = heapq.heappop(hq)
        if cur_node == end:
            break
        
        # if dist[cur_node] < cur_dist:
        #     continue
        
        for weight, adj_node in adj_list[cur_node]:
            new_dist = cur_dist + weight
            
            if dist[adj_node] > new_dist:
                heapq.heappush(hq, (new_dist, adj_node))
                dist[adj_node] = new_dist
    
    return dist[end]


V, E = map(int, input().split())
adj_list = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    adj_list[start].append((weight, end))
    adj_list[end].append((weight, start))
A, B = map(int, input().split())

answer1 = dijkstra(1, A) + dijkstra(A, B) + dijkstra(B, V)
answer2 = dijkstra(1, B) + dijkstra(B, A) + dijkstra(A, V)

if answer1 == float('inf') and answer2 == float('inf'):
    print(-1)
elif answer1 == float('inf'):
    print(answer2)
elif answer2 == float('inf'):
    print(answer1)
else:
    print(min(answer1, answer2))
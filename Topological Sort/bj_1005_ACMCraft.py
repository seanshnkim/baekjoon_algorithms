import sys
input = sys.stdin.readline
import heapq

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    in_degree = [0]*(V+1)
    weights = [0] + list(map(int, input().split()))
    acc_weights = weights.copy()
    q = []
    
    for _ in range(E):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        in_degree[Y] += 1
    
    target = int(input())
    
    for i in range(1, V+1):
        if in_degree[i] == 0:
            heapq.heappush(q, ((-1)*weights[i], i) )
    
    while q:
        w, cur_node = heapq.heappop(q)
        w *= -1
        
        if target == cur_node:
            break
        
        for adj_node in graph[cur_node]:
            in_degree[adj_node] -= 1
            if in_degree[adj_node] == 0:
                heapq.heappush(q, ( (-1)*weights[adj_node], adj_node ) )
                
            if acc_weights[adj_node] == weights[adj_node]:
                acc_weights[adj_node] += acc_weights[cur_node]
            elif acc_weights[cur_node] + weights[adj_node] > acc_weights[adj_node]:
                acc_weights[adj_node] = acc_weights[cur_node] + weights[adj_node]
    
    print(acc_weights[target])
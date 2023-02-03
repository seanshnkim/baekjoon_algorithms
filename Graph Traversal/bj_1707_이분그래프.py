import sys
sys.setrecursionlimit(100000)

n_test_cases = int(sys.stdin.readline())

def dfs(v, flag):
    if visited[v] != -1:
        return True
    
    visited[v] = flag
    for adj_v in adj_list[v]:
        if visited[adj_v] == -1:
            # if visited[v] == 0,  0^1 = 1 -> graph A
            # if visited[v] == 1,  1^1 = 0 -> graph B
            dfs(adj_v, flag^1)
        elif visited[adj_v] == visited[v]:
            return False
    return True
    

for _ in range(n_test_cases):
    V, E = map(int, sys.stdin.readline().split())
    
    adj_list = [[] for _ in range(V+1)]
    visited = [-1]*(V+1)
    for _ in range(E):
        v1, v2 = map(int, sys.stdin.readline().split())
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
    
    is_bipartite = True
    for v in range(1, V+1):
        if not dfs(v, 0):
            is_bipartite = False
            break
    print("YES" if is_bipartite else "NO")
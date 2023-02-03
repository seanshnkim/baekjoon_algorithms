import sys
sys.setrecursionlimit(100000)

V, E = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(V+1)]
visited = [False]*(V+1)

for e in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)


def dfs(v):
    visited[v] = True
    for adj_v in adj_list[v]:
        if not visited[adj_v]:
            dfs(adj_v)
    return

n_connected = 0
for v in range(1, V+1):
    if not visited[v]:
        dfs(v)
        n_connected += 1
print(n_connected)
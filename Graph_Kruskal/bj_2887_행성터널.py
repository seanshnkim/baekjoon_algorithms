import sys
input = sys.stdin.readline
import heapq

def cal_dist(xA, yA, zA, xB, yB, zB):
    return min(abs(xA-xB), abs(yA-yB), abs(zA-zB))

N = int(input())
planets = [list(map(int, input().split())) for _ in range(N)]

X_edges = []
Y_edges = []
Z_edges = []
for i in range(N):
    for j in range(i+1, N):
        x_diff = abs(planets[i][0] - planets[j][0])
        y_diff = abs(planets[i][1] - planets[j][1])
        z_diff = abs(planets[i][2] - planets[j][2])
        
        if len(X_edges) == N:
            heapq.heappushpop(X_edges, ((-1)*x_diff, i, j))
        else:
            heapq.heappush(X_edges, ((-1)*x_diff, i, j))
            
        if len(Y_edges) == N:
            heapq.heappushpop(Y_edges, ((-1)*y_diff, i, j))
        else:
            heapq.heappush(Y_edges, ((-1)*y_diff, i, j))
            
        if len(Z_edges) == N:
            heapq.heappushpop(Z_edges, ((-1)*z_diff, i, j))
        else:
            heapq.heappush(Z_edges, ((-1)*z_diff, i, j))


parent = [*range(N)]
rank = [0]*N
edges = []

for _, a, b in X_edges:
    edges.append((a, b, cal_dist(*planets[a], *planets[b])) )
for _, a, b in Y_edges:
    edges.append((a, b, cal_dist(*planets[a], *planets[b])) )
for _, a, b in Z_edges:
    edges.append((a, b, cal_dist(*planets[a], *planets[b])) )

edges.sort(key=lambda x: x[2])

def find(x):
    if parent[x] == x:
        return x
    
    root_x = find(parent[x])
    parent[x] = root_x
    return root_x


def rank_merge(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a == root_b:
        return False
    
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
        
    if rank[root_a] == rank[root_b]:
        rank[root_b] += 1
    
    return True

answer = 0
for a, b, w in edges:
    if rank_merge(a, b):
        answer += w
        
print(answer)

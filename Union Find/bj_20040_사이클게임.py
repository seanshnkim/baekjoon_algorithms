import sys
input = sys.stdin.readline

V, E = map(int, input().split())
parent = [*range(V)]
rank = [0]*V

def find(x):
    if parent[x] != x:
        x_root = find(parent[x])
        # 경로 압축
        parent[x] = x_root
        return x_root
    return x
    

def merge(x, y):
    x_root = find(x)
    y_root = find(y)
    
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[y_root] = x_root
    
    if rank[x_root] == rank[y_root]:
        rank[x_root] += 1

answer = 0
edges = [tuple(map(int, input().split())) for _ in range(E)]

for i in range(E):
    start, end = edges[i]
    
    start_root = find(start)
    end_root = find(end)
    if start_root == end_root:
        answer = i+1
        break
    
    if start_root != end_root:
        merge(start, end)

print(answer)
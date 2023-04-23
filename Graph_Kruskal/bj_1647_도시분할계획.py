import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

parent = [*range(V+1)]
rank = [0]*(V+1)

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
max_weight = 0
for a, b, w in edges:
    if rank_merge(a, b):
        answer += w
        max_weight = w

print(answer - max_weight)
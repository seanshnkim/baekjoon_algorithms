import sys
input = sys.stdin.readline

V, E = map(int, input().split())

rank = [0]*(V+1)
parent = [0]*(V+1)
edges = []
for _ in range(E):
    nodeA, nodeB, weight = map(int, input().split())
    edges.append((nodeA, nodeB, weight))
edges.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]

def find(x):
    if parent[x] == x:
        return x
    else:
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
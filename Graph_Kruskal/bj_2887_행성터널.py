import sys
input = sys.stdin.readline

def cal_dist(xA, yA, zA, xB, yB, zB):
    return min(abs(xA-xB), abs(yA-yB), abs(zA-zB))

N = int(input())
planets = [list(map(int, input().split())) for _ in range(N)]

edges = []
for i in range(N):
    for j in range(i+1, N):
        edges.append((i, j, cal_dist(*planets[i], *planets[j])) )

parent = [*range(N)]
rank = [0]*N

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

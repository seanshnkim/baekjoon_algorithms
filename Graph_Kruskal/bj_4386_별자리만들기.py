import sys
input = sys.stdin.readline
from math import sqrt

def cal_dist(x1, y1, x2, y2):
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )

N = int(input())
coordinates = [tuple(map(float, input().split())) for _ in range(N)]
edges = []
parent = [*range(N)]
rank = [0]*N

# 별 개수가 100개밖에 안되므로, 그냥 100*99 계산하기로
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        edges.append((i, j, cal_dist(x1, y1, x2, y2)))

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
import sys
input = sys.stdin.readline

N = int(input())
planets = [list(map(int, input().split())) + [i] for i in range(N)]
edges = []

for c in range(3):
    # x,y,z 좌표에 대해 정렬
    planets.sort(key=lambda x: x[c])
    for i in range(1, N):
        # 각 x좌표 간 거리 차이를 구하여 edges에 저장, 어쨌든 여기서 두 점 사이 거리는 
        # x좌표 간 거리 차이 또는 y좌표 간 거리 차이 또는 z좌표 간 거리 차이 이 셋 중 하나로 정의되었으므로.
        diff = abs(planets[i][c]-planets[i-1][c])
        idx_A = planets[i-1][3]
        idx_B = planets[i][3]
        edges.append((diff, idx_A, idx_B) )

parent = [*range(N)]
rank = [0]*N
edges.sort()


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
for w, a, b in edges:
    if rank_merge(a, b):
        answer += w
        
print(answer)
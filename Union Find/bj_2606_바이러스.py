# 2022-07-13, Sehyun Kim
import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

# parent = [0] * (V+1)
parent = [i for i in range(V+1)]
rank = [0] * (V+1)

def find(x):
    if parent[x] == x:
        return x
    else:
        root_x = find(parent[x])
        # 시간복잡도 O(N)인 naive_find의 문제점을 해결
        # 경로 압축!
        parent[x] = root_x
        return root_x


def rank_merge(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a == root_b:
        return
    
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
    
    if rank[root_a] == rank[root_b]:
        rank[root_b] += 1


for _ in range(E):
    s, e = map(int, sys.stdin.readline().split())
    rank_merge(s, e)

root_1 = parent[1]
# answer = sum([1 for p in parent if p == root_1]) - 1
answer = parent.count(root_1) - 1
print(answer)
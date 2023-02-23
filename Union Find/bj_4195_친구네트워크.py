import sys
input = sys.stdin.readline
from collections import defaultdict

def find(x):
    if parent[x] != x:
        # return find(parent[x])
        
        # 경로 압축
        root_x = find(parent[x])
        parent[x] = root_x
        return root_x
    return x

def merge(x, y):
    x_root = find(x)
    y_root = find(y)
    
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
        counts[x_root] += 1
    else:
        parent[x_root] = y_root
        counts[y_root] += 1
    if rank[x_root] == rank[y_root]:
        rank[y_root] += 1



N_testcase = int(input())
for _ in range(N_testcase):
    E = int(input())
    cnt = 1
    parent = {}
    counts = defaultdict(lambda: 1)
    rank = defaultdict(int)
    for _ in range(E):
        start_ID, end_ID = input().split()
        if start_ID not in parent:
            parent[start_ID] = start_ID
        if end_ID not in parent:
            parent[end_ID] = end_ID
        
        merge(start_ID, end_ID)
        
        print(counts[parent[end_ID]])
        
        
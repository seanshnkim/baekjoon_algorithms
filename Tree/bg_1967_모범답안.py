import sys
from collections import deque

num_node = int(input())
tree = {}
for n in range(num_node):
    tree[n+1] = {}

for _ in range(num_node-1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    tree[parent][child] = weight

max_diam = 0

def dfs(n, d):
    if len(tree[n]) == 0:
        return 0
    left, right = 0, 0
    for c in tree[n]:
        # 이래서 이중 리스트, 이중 딕셔너리 쓰지 말라는 건가?
        r = dfs(c, tree[n][c])
        if left <= right:
            left = max(left, r)
        else:
            right = max(right, r)
    
    global max_diam
    max_diam = max(max_diam, left+right)
    return max(left + d, right + d)

dfs(1,0)
print(max_diam)
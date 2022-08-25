import sys
from collections import deque

num_node = int(input())

tree = {}
for n in range(num_node):
    tree[n+1] = {}

for _ in range(num_node-1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    tree[parent][child] = weight

# search
def dfs(tree, n, visited):
    if len(tree[n]) == 0 or visited[n]:
        return 0
    else:
        visited[n] = True
        childrens_weight = tree[n]
        curr_diameters = []
        for c in childrens_weight:
            if not visited[c]:
                curr_diameters.append(tree[n][c] + dfs(tree, c, visited))
        return max(curr_diameters)

visited = [False for _ in range(num_node+1)]

ans_list = []
for c in tree[1]:
    ans_list.append(tree[1][c] + dfs(tree, c, visited))
ans_list.sort()
print(sum(ans_list[:2]))


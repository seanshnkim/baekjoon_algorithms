import sys
from collections import deque

node_num = int(sys.stdin.readline())
# each index of "parents" list is equal to node(ranging from 0 ~ node_num-1)
# parents[n] is equal to parent node of node n
parents = list(map(int, sys.stdin.readline().split()))

# For each node n, tree[n] is equal to list of child nodes of node n
# if tree[n] is empty, node n is leaf node
tree = [[] for _ in range(node_num)]

for node in range(node_num):
    for i, p in enumerate(parents):
        if p == node:
            tree[node].append(i)

node_delete = int(sys.stdin.readline())

count = 0
def dfs(node, node_del):
    #NOTE: if the only remaining node is root node?
    if node == node_del:
        return 0
    queue = deque([node])
    global count
    while queue:
        node = queue.popleft()
        if not tree[node]:
            return 1
        else:
            for c in tree[node]:
                count += dfs(c, node_del)
    return count

print(dfs(0, node_delete))


import sys
sys.setrecursionlimit(10 ** 9)

num_node = int(input())
tree = {}
for n in range(num_node):
    tree[n+1] = []

# Why symmetric? -> to search from top-down, and bottom-up
for _ in range(num_node-1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    tree[parent].append((child, weight))

def dfs(start_node):
    if len(tree[start_node]) == 0:
        return 0
    distances =[]
    for child, weight in tree[start_node]:
        distances.append(dfs(child) + weight)
    return max(distances)

dist = []
for c, w in tree[1]:
    dist.append(dfs(c) + w)
dist.sort(reverse=True)
print(dist[0] + dist[1])
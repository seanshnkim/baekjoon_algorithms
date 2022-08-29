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
    tree[child].append((parent, weight))

# Only single list is needed for "visited" and "updated maximum distance".
# I think setting -1 as false value for unvisited state and else positive integers for the updated distances is a smart way.
curr_diameters = [-1 for _ in range(num_node+1)]
curr_diameters[1] = 0

# This dfs function does not return any value, yet updates list(curr_diameters)
def dfs(start_node, start_weight):
    for (child, child_weight) in tree[start_node]:
        if curr_diameters[child] == -1:
            curr_diameters[child] = start_weight + child_weight
            dfs(child, start_weight + child_weight)

# after the first dfs, we get the farthest node from root node(1) and its distance
dfs(1,0)
farthest_node = curr_diameters.index(max(curr_diameters))

# initialize it again
curr_diameters = [-1 for _ in range(num_node+1)]
curr_diameters[farthest_node] = 0
dfs(farthest_node, 0)

print(max(curr_diameters))

'''This algorithm computes dfs twice, but it returns the maximum distance
regardless of tree structure(wheter it is binary, or something else.'''

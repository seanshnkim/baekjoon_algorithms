import sys
sys.setrecursionlimit(100000)

'''
1. If parent has only one child node and the only child node is to be deleted
2. Edge case: If only one node(=root node) is given
'''

node_num = int(sys.stdin.readline())
# each index of "parents" list is equal to node(ranging from 0 ~ node_num-1)
# parents[n] is equal to parent node of node n
parents = list(map(int, sys.stdin.readline().split()))
root_node = parents.index(-1)

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
    global count
    if node == node_del:
        # if node is to be deleted, then update tree state
        # if node has no parent(which is root node), then pass
        if parents[node] != -1:
            tree[parents[node]].remove(node)
        return 0
    # If tree[node] is empty, then it will skip for loop and go to if statement directly.
    children = tree[node].copy()
    # Note that tree[node] in the for loop is changed before for loop ends.
    # for c in tree[node]:
    for c in children:
        dfs(c, node_del)
        '''If the node had only one child node which has been deleted, 
        then return 1(count itself as leaf node)'''
    if not tree[node]:
        count += 1
        return 1
    # count only increases when meet leaf node!!
    # return count

# dfs(0, node_delete)
dfs(root_node, node_delete)
print(count)


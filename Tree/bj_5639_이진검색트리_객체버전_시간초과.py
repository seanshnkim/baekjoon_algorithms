# 객체로 구현했고, 트리를 직접 만들어서 구현했기 때문에 시간이 오래 걸렸다

import sys
sys.setrecursionlimit(10**6)

class BSTNode:
    def __init__(self, n):
        self.val = n
        self.left = None
        self.right = None

def insert_node(parent, node2insert):
    if node2insert.val < parent.val:
        if parent.left is None:
            parent.left = node2insert
        else:
            insert_node(parent.left, node2insert)
    else:
        if parent.right is None:
            parent.right = node2insert
        else:
            insert_node(parent.right, node2insert)

i = 0
root = None
while True:
    try:
        n = int(sys.stdin.readline())
        curr_node = BSTNode(n)
        # node_list.append(curr_node)
        if i == 0:
            root = curr_node
        else:
            insert_node(root, curr_node)
        i += 1
    except:
        break

def dfs(root_node):
    if root_node.left is None and root_node.right is None:
        return [root_node.val]
    elif root_node.left is None:
        return dfs(root_node.right) + [root_node.val]
    elif root_node.right is None:
        return dfs(root_node.left) + [root_node.val]
    else:
        return dfs(root_node.left) + dfs(root_node.right) + [root_node.val]


print(*dfs(root), sep='\n')
import sys

class Node():
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

num_node = int(input())
tree = {}
for _ in range(num_node):
    root, left, right = sys.stdin.readline().split()
    tree[root] = Node(root, left, right) 

def preorder(node):
    ans = node.root
    if node.left != '.':
        ans += preorder(tree[node.left])
    if node.right != '.':
        ans += preorder(tree[node.right])
    return ans

def inorder(node):
    ans = ''
    if node.left != '.':
        ans += inorder(tree[node.left])
    ans += node.root
    if node.right != '.':
        ans += inorder(tree[node.right])
    return ans
        
def postorder(node):
    ans = ''
    if node.left != '.':
        ans += postorder(tree[node.left])
    if node.right != '.':
        ans += postorder(tree[node.right])
    ans += node.root
    return ans

print(preorder(tree['A']))
print(inorder(tree['A']))
print(postorder(tree['A']))
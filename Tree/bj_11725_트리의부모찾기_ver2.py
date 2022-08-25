import sys
from collections import deque

# num_node = int(input())
# node_info = {}
# for _ in range(num_node-1):
#     node1, node2 = map(int, (sys.stdin.readline().split()))
#     if node1 in node_info:
#         node_info[node1].append(node2)
#     else:
#         node_info[node1] = [node2]
#     if node2 in node_info:
#         node_info[node2].append(node1)
#     else:
#         node_info[node2] = [node1]
num_node = int(input())
node_info = {}
for i in range(1, num_node+1):
    node_info[i] = []
for _ in range(num_node-1):
    node1, node2 = map(int, sys.stdin.readline().split())
    node_info[node1].append(node2)
    node_info[node2].append(node1)

parent_nodes = [0 for _ in range(num_node+1)]
queue = deque([1])

while queue:
    curr_node = queue.popleft()
    neighbors = node_info[curr_node]
    for n in neighbors:
        # if n is not root node and n does not have parent node yet:
        if n != 1 and parent_nodes[n] == 0:
            parent_nodes[n] = curr_node
            queue.append(n)

print(*parent_nodes[2:], sep='\n')

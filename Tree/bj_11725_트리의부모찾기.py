import sys
from collections import deque

num_node = int(input())
node_info = {}
for _ in range(num_node-1):
    node1, node2 = map(int, (sys.stdin.readline().split()))
    if node1 in node_info:
        node_info[node1].append(node2)
    else:
        node_info[node1] = [node2]
    if node2 in node_info:
        node_info[node2].append(node1)
    else:
        node_info[node2] = [node1]

class Node():
    def __init__(self, root, parent):
        self.root = root
        self.parent = parent

visited_nodes = [False for x in range(num_node+1)]
visited_nodes[0] = True

curr_node = 1
root_queue = deque()
parent_info = {}
visited_nodes[curr_node] = True
while False in visited_nodes:
    connected_nodes = node_info[curr_node]
    for node in connected_nodes:
        if visited_nodes[node] == False:
            parent_info[node] = curr_node
        visited_nodes[node] = True
        root_queue.append(node)
    curr_node = root_queue.popleft()

ans = [x[1] for x in sorted(parent_info.items())]
print(*ans, sep='\n')
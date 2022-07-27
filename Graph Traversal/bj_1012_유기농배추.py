# 2022-07-17, Sehyun Kim
import sys
from collections import deque

nTestCase = int(input())

def bfs(adjNodeList, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        
        for adjNode in adjNodeList[v]:
            if not visited[adjNode]:
                queue.append(adjNode)
                visited[adjNode] = True
    return 0


for _ in range(nTestCase):
    width, length, nOnes = map(int, sys.stdin.readline().split())
    nNode = width * length

    visited = [False for _ in range(nNode)]
    adjNodeList = [[-1] for _ in range(nNode)]

    for _ in range(nOnes):
        i, j = map(int, sys.stdin.readline().split())
        idx_flat_1D = (j * width) + i
        # if 1, then replace -1 with idx_flat_id(current idx in flattened 1D map)
        adjNodeList[idx_flat_1D][0] = idx_flat_1D
    
    # 항상 1차원 배열과 2차원 배열 indexing이 헷갈리니 주의하자.
    for i in range(nNode):
        if adjNodeList[i][0] != -1:
            adjNodes = []
            if (i < width * (length - 1) and adjNodeList[i + width][0] != -1):
                adjNodes.append(i + width)
            if i >= width and adjNodeList[i - width][0] != -1:
                adjNodes.append(i - width)
            if (i % width) != 0 and adjNodeList[i-1][0] != -1:
                adjNodes.append(i - 1)
            if (i % width) != width - 1 and adjNodeList[i+1][0] != -1:
                adjNodes.append(i + 1)
            
            adjNodeList[i].extend(adjNodes)
    
    nGraph = 0
    for node in range(nNode):
        # if the current node is unvisited and has value 1(a region to be searched)
        if not visited[node] and adjNodeList[node][0] != -1:
            bfs(adjNodeList, visited, node)
            nGraph += 1
    
    print(nGraph)


'''
Result:
0 0 0 0 1 
0 0 0 0 0
1 1 1 1 1

Input:
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
'''
# 2022-07-13, Sehyun Kim
import sys
from collections import deque

sizeOfMap = int(input())
sqrMap = []

for _ in range(sizeOfMap):
    sqrMap.append(sys.stdin.readline().rstrip('\n'))

'''if sqrMap[i][j] == 1, for sqrMap[i][j] its adjacent nodes(adjNode) =
    [
    sqrMap[i][j-1]      (but only if j > 0),
    sqrMap[i][j+1]      (but only if j < sizeOfMap)
    OR sqrMap[i-1][j]   (but only if i > 0),
    OR sqrMap[i+1][j] (but only if i < sizeOfMap),
    ]
    if adjNode == 1 then do BFS(ajdNode)
'''

'''
    if  j == 0:
        skip searching (i, j-1)
    if j == sizeOfMap:
        skip searching (i, j+1)
    if i == 0:
        skip searching (i-1, j)
    if i == sizeOfMap:
        skip searching (i+1, j)
'''

# Given input is a simple 2D map, and they are lists of strings(e.g 0011101, 1001110...)
# The code below converts the given 2D map into a list of adjacent nodes(adjNodeList). 
# If one side of square map is equal to 7, length of the list is 7*7 = 49 since the map has total 49 nodes.
numNode = sizeOfMap ** 2
adjNodeList = [[] for _ in range(numNode)]
visited = [False for _ in range(numNode)]

# convert the given 2D string map into a list of adjacent nodes, making it easy to perform BFS
for i in range(sizeOfMap):
    for j in range(sizeOfMap):
        currIdx = i*sizeOfMap + j
        # add current node(start) to adjNodes as well (자기 자신 노드를 인접 노드 리스트에 추가한다)
        adjNodes = [currIdx]
        if sqrMap[i][j] == '1':
            if j != 0 and sqrMap[i][j-1] == '1':
                adjNodes.append(currIdx - 1)
            if j != sizeOfMap-1 and sqrMap[i][j+1] == '1':
                adjNodes.append(currIdx + 1)
            if i != 0 and sqrMap[i-1][j] == '1':
                adjNodes.append(currIdx - sizeOfMap)
            if i != sizeOfMap-1 and sqrMap[i+1][j] == '1':
                adjNodes.append(currIdx + sizeOfMap)
        
            adjNodeList[currIdx].extend(adjNodes)
        else:
            # 어떻게 0인 노드를 구별할 것인가? ==> 80번째 줄
            adjNodeList[currIdx].append(-1)


def bfs(adjNodeList, visited, start):
    cnt = 0
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        cnt += 1
        
        for adjNode in adjNodeList[v]:
            if not visited[adjNode]:
                queue.append(adjNode)
                visited[adjNode] = True
    return cnt

cntConNodeList = []
cntSubgraph = 0
for n in range(numNode):
    
    if not visited[n] and adjNodeList[n][0] != -1:
        cntSubgraph += 1
        cntConNodeList.append(bfs(adjNodeList, visited, n))

print(cntSubgraph)

sortedConNodeList = sorted(cntConNodeList)
for c in sortedConNodeList:
    print(c)

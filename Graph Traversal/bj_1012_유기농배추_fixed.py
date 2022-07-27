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
    # 0이 있는 것과 자기 자신이 1이고 isolated graph인 경우를 어떻게 구별할 것인가?
    adjNodeList = [[] for _ in range(nNode)]
    # map2D = ['0' * width for _ in range(length)]
    map2D = [[0 for _ in range(width)] for _ in range(length)]

    for _ in range(nOnes):
        i, j = map(int, sys.stdin.readline().split())
        idx_flat_1D = (j * width) + i
        # 'str' object does not support item assignment
        # map2D[j][i] = '1'
        map2D[j][i] = 1
    
    # 항상 1차원 배열과 2차원 배열 indexing이 헷갈리니 주의하자.
    for l in range(length):
        for w in range(width):
            if map2D[l][w] == 1:
                currIdx = l * width + w
                adjNodes = [currIdx]
                if l != length-1 and map2D[l+1][w] == 1:
                    adjNodes.append(currIdx + width)
                if l != 0 and map2D[l-1][w] == 1:
                    adjNodes.append(currIdx - width)
                if w != width-1 and map2D[l][w+1] == 1:
                    adjNodes.append(currIdx + 1)
                if w != 0 and map2D[l][w-1] == 1:
                    adjNodes.append(currIdx - 1)
                
                # adjNodeList[i].extend(adjNodes) ==> 실수를 방지하려면 iterator 변수명을 신중하게 정해야 한다.
                adjNodeList[currIdx].extend(adjNodes)
        
    nGraph = 0
    for node in range(nNode):
        # if the current node is unvisited and adjNodeList is not empty(if empty, is equal to 0)
        if not visited[node] and adjNodeList[node]:
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
import sys
input = sys.stdin.readline
from collections import deque

'''
답이 여럿일 경우에는 아무거나 하나를 출력 한다. 만약 남일이가 순서를 정하는 것이 불가능할 경우에는 첫째 줄에 0을 출력한다.
'''
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
in_degree = [0]*(N+1)
orders = []

for _ in range(M):
    length, *seq = list(map(int, input().split()))
    orders.append(seq)
    for i in range(1, length):
        in_degree[seq[i]] += 1
        graph[seq[i-1]].append(seq[i])
    

# FIXME - 첫번째로 이게 문제였고
# roots = deque()
# for m in range(M):
#     if in_degree[orders[m][0]] == 0:
#         roots.append(orders[m][0])
# FIXME - 굳이 set으로 만들 필요도 없다. 이렇게 하면 
# isolated된 노드에 대해서도 따로 처리해줘야 하기 때문이다.
# roots = set()
# for m in range(M):
#     if in_degree[orders[m][0]] == 0:
#         roots.add(orders[m][0])

roots = deque(list(roots))
visited = [False]*(N+1)
answer = []
cnt = 0
while roots:
    cur_root = roots.popleft()
    answer.append(cur_root)
    visited[cur_root] = True
    cnt += 1
    
    for adj_node in graph[cur_root]:
        in_degree[adj_node] -= 1
        if in_degree[adj_node] == 0:
            roots.append(adj_node)

if cnt == N:
    print(*answer, sep='\n')
else:
    is_cycle = False
    isolated = []
    for i in range(1, N+1):
        if in_degree[i] > 0:
            is_cycle = True
            print(0)
            break
        elif not visited[i]:
            isolated.append(i)
            
    if not is_cycle:
        print(*(answer+isolated), sep='\n')
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

stack = [1]
cnts = 0
answer = "YES"

while stack:
    top = stack.pop()
    
    # leaf node에 도달했다면
    if not graph[top]:
        if cnts < E:
            answer = "NO"
        break
    else:
        stack.append(top)
        adj_node = graph[top].pop()
        stack.append(adj_node)
        cnts += 1
        # graph[adj_node].remove(top)
        graph[adj_node].remove(top)

print(answer)

# 반례:
'''
3 5
1 2
2 1
1 3
3 2
2 3
'''
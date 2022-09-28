import sys
sys.setrecursionlimit(1000000)

num_vertex = int(input())

tree = [[] for _ in range(num_vertex+1)]
'''NOTE:# There is no guarantee if root node is 1
parent-child pair is not defined in input. If node a is connected to b, it is not always that a is the parent of node b.
Solution: save for both: 
1) a is connected to b: tree[a] = [b, ...]   
2) b is connected to a: tree[b] = [a, ...]
'''
for _ in range(num_vertex):
    input_line = list(map(int, sys.stdin.readline().split()))
    node = input_line[0]
    for i in range(1, len(input_line)-1, 2):
        tree[node].append((input_line[i], input_line[i+1]))
        tree[input_line[i]].append((node, input_line[i+1]))
for n in range(1, num_vertex+1):
    tree[n] = list(set(tree[n]))



#NOTE: https://www.acmicpc.net/board/view/54434
visited = [1] + [0 for _ in range(num_vertex)]
def dfs(ver):
    global answer
    visited[ver] = 1
    if tree[ver]:
        max_1st_dist, max_2nd_dist = 0, 0
        for child, weight in tree[ver]:
            if visited[child]:
                continue
            curr_dist = dfs(child) + weight
            if curr_dist > max_1st_dist:
                max_2nd_dist, max_1st_dist = max_1st_dist, curr_dist
            elif curr_dist > max_2nd_dist:
                max_2nd_dist = curr_dist
        answer = max(answer, max_1st_dist+max_2nd_dist)
        return max_1st_dist
    else:
        return 0

answer = 0

dfs(1)
print(answer)


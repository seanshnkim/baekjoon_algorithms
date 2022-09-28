import sys
sys.setrecursionlimit(1000000)

num_vertex = int(input())

tree = [[] for _ in range(num_vertex+1)]

for _ in range(num_vertex):
    input_line = list(map(int, sys.stdin.readline().split()))
    curr_vertex = input_line[0]
    for i in range(1, len(input_line)-1, 2):
        tree[curr_vertex].append((input_line[i], input_line[i+1]))

#NOTE: https://www.acmicpc.net/board/view/54434
def dfs(ver):
    global answer
    if tree[ver]:
        max_1st_dist, max_2nd_dist = 0, 0
        for child, weight in tree[ver]:
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


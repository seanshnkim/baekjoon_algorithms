import sys
input = sys.stdin.readline

n_city = int(input())
n_plan = int(input())
parent = [*range(n_city)]
rank = [0]*n_city


def find(x):
    if parent[x] == x:
        return x
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return root_x


def rank_merge(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a == root_b:
        return
    
    # REVIEW - if rank[root_a] > rank[root_b]: -> 로 할 때는 답이 틀리게 나왔다?
    if rank[root_a] >= rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
    
    if rank[root_a] == rank[root_b]:
        # rank[root_b] += 1
        rank[root_a] += 1


for i in range(n_city):
    ith_adj_vertices = list(map(int, input().split()))
    for j in range(n_city):
        if ith_adj_vertices[j] == 1:
            rank_merge(i, j)


plan = list(map(int, input().split() ) )
# 문제에서 주어진 도시는 1부터 시작하므로, 0번째 도시를 1이 아니라 0으로 맞춘다.
plan = [i-1 for i in plan]

answer = "YES"
for p in range(n_plan-1):
    if parent[plan[p]] != parent[plan[p+1]]:
        answer = "NO"
        break
    
print(answer)

'''
반례:
4
4
0 0 0 1
0 0 1 0
0 1 0 1
1 0 1 0
3 1 2 4
output: NO
answer: YES
'''
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, num):
        self.num = num
        self.parents = []


N = int(input())
costs = [0]
nodes = [None] + [Node(i) for i in range(1, N+1)]
for i in range(1, N+1):
    inputs = list(map(int, input().split()))
    costs.append(inputs[0])
    
    for j in range(1, len(inputs)-1):
        nodes[inputs[j]].children.append(i)
        nodes[i].parents.append(inputs[j])
    

# root node 걸리는 시간은 항상 해당 root node의 각 시간과 같다
dp = [0]*(N+1)
visited = [False]*(N+1)

def dfs(idx):
    # if root
    if not nodes[idx].parents:
        dp[idx] = costs[idx]
        visited[idx] = True
    else:
        max_acc_cost = 0
        for idx_parent in nodes[idx].parents:
            if not visited[idx_parent]:
                dfs(idx_parent)
                # 반드시 parent를 마무리하고 cur_node를 실행해야 하므로 최대를 골라야 한다.
            # if dp[idx] == 0 or dp[idx] < dp[idx_parent] + costs[idx]:
            #     dp[idx] = dp[idx_parent] + costs[idx]
            max_acc_cost = max(dp[idx_parent], max_acc_cost)
        dp[idx] = max_acc_cost + costs[idx]
            
        visited[idx] = True

for idx in range(1, N+1):
    dfs(idx)

for i in range(1, N+1):
    print(dp[i])
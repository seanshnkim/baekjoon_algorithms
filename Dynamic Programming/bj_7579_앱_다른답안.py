N, M = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
sum_costs = sum(costs)

dp = [[0 for _ in range(sum(costs)+1)] for _ in range(N+1)]
    
for i in range(1, N+1):
    mem, cost = memories[i], costs[i]
    
    for c in range(1, sum_costs+1):
        if c < cost:
            dp[i][c] = dp[i-1][c]
        else:
            dp[i][c] = max(mem+dp[i-1][c-cost], dp[i-1][c])


for i in range(sum_costs+1):
    if dp[-1][i] >= M:
        print(i)
        break
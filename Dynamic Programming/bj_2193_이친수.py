import sys

N = int(sys.stdin.readline())
dp = [[0,0] for _ in range(N+1)]
dp[1] = [0, 1]

if N > 1:
    for k in range(2, N+1):
        dp[k][0] = dp[k-1][0] + dp[k-1][1]
        dp[k][1] = dp[k-1][0]
print(sum(dp[N]))
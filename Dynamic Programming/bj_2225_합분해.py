import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[0]*K for _ in range(N+1)]
for i in range(N+1):
    dp[i][1] = 1

for n in range(1, N+1):
    for i in range(2, K+1):
        for j in range(1, i):
            for m in range(0, n+1):
                dp[n][i] += dp[n-m][i-j] + dp[m][j]

print(dp[N][K])


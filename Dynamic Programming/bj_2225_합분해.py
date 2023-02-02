import sys

# FIXME - 모든 걸 저장할 이유는 없다
N, K = map(int, sys.stdin.readline().split())
# dp = [[0]*K for _ in range(N+1)]
# for i in range(N+1):
#     dp[i][1] = 1

# for n in range(1, N+1):
#     for i in range(2, K+1):
#         for j in range(1, i):
#             for m in range(0, n+1):
#                 dp[n][i] += dp[n-m][i-j] + dp[m][j]

# print(dp[N][K])
dp = [[0]*(N+1) for i in range(K+1)]
for j in range(N+1):
    dp[1][j] = 1

for k in range(2, K+1):
    for n in range(N+1):
        for j in range(n+1):
            #REVIEW - 이건 왜 답이 다르게 나오는가? 
            # dp[k][n] += dp[k-1][n-j] % 1000000000
            dp[k][n] += dp[k-1][n-j]
        dp[k][n] %= 1000000000

print(dp[K][N])
import sys

N = int(sys.stdin.readline())
modM = 10007

dp = [[0]*10 for _ in range(N+1)]
for i in range(10):
    dp[1][i] = 1


for n in range(2, N+1):
    for k in range(10):
        dp[n][k] = sum(dp[n-1][i] for i in range(k+1))
        dp[n][k] %= modM

print(sum(dp[N]) % modM)
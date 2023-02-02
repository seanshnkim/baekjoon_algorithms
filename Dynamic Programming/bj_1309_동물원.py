import sys

modM = 9901
N = int(sys.stdin.readline())
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 3

for i in range(2, N+1):
    dp[i] = dp[i-2] * 2 + (dp[i-1] - dp[i-2]) + dp[i-1]
    dp[i] %= modM

print(dp[N])
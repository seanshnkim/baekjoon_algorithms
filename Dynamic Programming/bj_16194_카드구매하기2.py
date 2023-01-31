import sys

N = int(sys.stdin.readline())
prices = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = dp[i-1]+prices[1]
    for j in range(2, i+1):
            dp[i] = min(dp[i], dp[i-j]+prices[j])

print(dp[N])
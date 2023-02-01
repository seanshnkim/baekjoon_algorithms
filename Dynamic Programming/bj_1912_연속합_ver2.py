import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N)]
dp[0] = nums[0]

for i in range(1, N):
    if dp[i-1] > 0:
        dp[i] = dp[i-1] + nums[i]
    else:
        dp[i] = nums[i]

print(max(dp))
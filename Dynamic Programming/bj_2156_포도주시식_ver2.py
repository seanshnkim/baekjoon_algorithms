import sys

N = int(sys.stdin.readline())
nums = [0]
for n in range(N):
    nums.append(int(sys.stdin.readline()))

dp = [[0]*3 for _ in range(N+1)]
dp[1] = [0, nums[1], 0]
if N >= 2:
    dp[2] = [nums[1], nums[2], nums[1]+nums[2]]

for n in range(3, N+1):
    dp[n][0] = max(dp[n-1])
    dp[n][1] = dp[n-1][0] + nums[n]
    dp[n][2] = dp[n-1][1] + nums[n]

print(max(dp[N]))

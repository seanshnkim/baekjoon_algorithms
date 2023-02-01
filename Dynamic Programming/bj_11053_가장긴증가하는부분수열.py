import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    for prev_idx in range(i-1, -1, -1):
        if nums[i] > nums[prev_idx]:
            dp[i] = max(dp[prev_idx]+1, dp[i])
    if dp[i] == 0:
        dp[i] = 1

# FIXME - dp[N-1]은 dp[0:N] 중 최댓값이라고 보장할 수 없다.
# print(dp[N-1])
print(max(dp))

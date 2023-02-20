import sys
input = sys.stdin.readline

N = int(input())
MAX_NUM = 100000

dp = [-1]*(MAX_NUM+1)
dp[2] = dp[5] = 1
dp[4] = 2

for i in range(6, N+1):
    # if i-2 != -1 and i-5 != -1:
    #     dp[i] = min(dp[i-2]+1, dp[i-5]+1)
    if dp[i-2] == -1:
        dp[i] = dp[i-5]+1
    elif dp[i-5] == -1:
        dp[i] = dp[i-2]+1
    else:
        dp[i] = min(dp[i-2], dp[i-5])+1

print(dp[N])
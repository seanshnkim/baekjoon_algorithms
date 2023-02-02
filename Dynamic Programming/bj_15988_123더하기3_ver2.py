import sys

MAX_N = 1000000
modM = 1000000009

dp = [0]*(MAX_N+1)
#REVIEW - dynamic programming에선 그만큼 초기화가 중요하다
dp[0] = 1

for i in range(1, MAX_N+1):
    if i-1 >= 0:
        dp[i] += dp[i-1]
    if i-2 >= 0:
        dp[i] += dp[i-2]
    if i-3 >= 0:
        dp[i] += dp[i-3]
    dp[i] %= modM

n_test_case = int(sys.stdin.readline())
for t in range(n_test_case):
    N = int(sys.stdin.readline())
    print(dp[N])
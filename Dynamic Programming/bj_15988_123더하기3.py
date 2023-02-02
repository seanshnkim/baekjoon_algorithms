import sys

MAX_N = 1000000
modM = 1000000009

dp = [[0]*4 for _ in range(MAX_N+1)]
dp[1] = [0,1,0,0]
dp[2] = [0,1,1,0]
dp[3] = [0,2,1,1]

for i in range(4, MAX_N+1):
    for k in range(1, 4):
        dp[i][k] += sum(dp[i-k]) % modM

n_test_case = int(sys.stdin.readline())
for t in range(n_test_case):
    N = int(sys.stdin.readline())
    print(sum(dp[N]))
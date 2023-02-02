import sys

MAX_N = 1000000
modM = 1000000009

dp = [[0]*4 for _ in range(MAX_N+1)]
# FIXME - 정수 n이 3 이하이고 n을 1,2,3의 합으로 나타낼 때, 
# n 홀로 쓰이는 건 경우의 수로 간주하지 않는다.
# dp[2] = [0,1,1,0]
# dp[3] = [0,2,1,1]
dp[1] = [0,0,0,0]
dp[2] = [0,1,0,0]
dp[3] = [0,2,1,0]

for i in range(4, MAX_N+1):
    for k in range(1, 4):
        if (i-k) <= 3:
            dp[i][k] += (sum(dp[i-k]) + 1) % modM
        else:
            dp[i][k] += sum(dp[i-k]) % modM

n_test_case = int(sys.stdin.readline())
for t in range(n_test_case):
    N = int(sys.stdin.readline())
    print(sum(dp[N]))
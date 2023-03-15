import sys
input = sys.stdin.readline
MAX_L = 5000
# 홀수는 모두 방법의 가짓수가 0이므로 2500+1개 칸만 준비하면 된다.
dp = [[-1, -1] for _ in range(MAX_L//2+1)]
# 사실 dp[2]에 해당
dp[1] = [1,0]
dp[2] = [1,1]

for i in range(2, MAX_L//2):
    dp[i+1][0] = dp[i][0] + dp[i][1]
    dp[i+1][1] = dp[i][0] * 2 + dp[i][1]


T = int(input())
for _ in range(T):
    L = int(input())
    if L % 2 == 1:
        print(0)
    else:
        print(sum(dp[L//2]))
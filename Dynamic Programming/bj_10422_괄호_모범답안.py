import sys
input = sys.stdin.readline
MAX_L = 5000
divisor = 1000000007
# 홀수는 모두 방법의 가짓수가 0이므로 2500+1개 칸만 준비하면 된다.
dp = [0]*(MAX_L//2+1)
dp[0] = 1

for n in range(1, MAX_L//2+1):
    for j in range(1, n+1):
        dp[n] += dp[j - 1] * dp[n - j]
    dp[n] %= divisor

T = int(input())
for _ in range(T):
    L = int(input())
    if L % 2 == 1:
        print(0)
    else:
        print(dp[L//2])


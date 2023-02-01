import sys

MAX_CNT = 100000
N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]
dp[1] = 1

for i in range(2, N+1):
    if i**2 <= N:
        dp[i**2] = 1
    if dp[i] == 1:
        continue
    
    sqr_idx = 1
    if dp[i] == 0:
        dp[i] = MAX_CNT
    while sqr_idx**2 < i:
        dp[i] = min(dp[i], dp[i-sqr_idx**2] + 1)
        sqr_idx += 1
    

print(dp[N])
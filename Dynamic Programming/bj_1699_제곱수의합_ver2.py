import sys

N = int(sys.stdin.readline())
dp = [i for i in range(N+1)]

for i in range(1, N+1):
    # if i**2 <= N:
    #     dp[i**2] = 1
        
    # if dp[i] == 1:
    #     continue

    k = 1
    while k*k <= i:
        if dp[i-k*k]+1 < dp[i]:
            dp[i] = dp[i-k*k]+1
        k += 1
    
print(dp[N])
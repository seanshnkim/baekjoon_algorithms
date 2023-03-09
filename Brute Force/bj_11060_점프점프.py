import sys
input = sys.stdin.readline

N = int(input())
jumps = list(map(int, input().split()))
dp = [-1]*N
dp[0] = 0

for i in range(N):
    jump = jumps[i]
    for j in range(1, jump+1):
        if i+j == N:
            break
        if dp[i+j] == -1:
            dp[i+j] = dp[i]+1
        else:
            dp[i+j] = min(dp[i+j], dp[i]+1)

print(dp[-1])

'''반례:
3
0 2 3
정답: -1
출력 결과: 0
'''
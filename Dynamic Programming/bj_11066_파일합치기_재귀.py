import sys
input = sys.stdin.readline
from itertools import accumulate


def dfs(start, end):
    if end - start == 1:
        dp[start][end] = numbers[start] + numbers[end]
        return 
    if end == start:
        return
    
    for i in range(start, end):
        # 이건 포함이다. 포함. dp[n][k] -> 이면 n번째 이상 k번째 이하의 수열이라는 뜻.
        # dp[start][i] + dp[i+1][end] 비교
        if dp[start][i] == 0:
            dfs(start, i)
        if dp[i+1][end] == 0:
            dfs(i+1, end)
            
        if dp[start][end] == 0 or dp[start][end] > dp[start][i] + dp[i+1][end]:
            dp[start][end] = dp[start][i] + dp[i+1][end]
    
    dp[start][end] += (acc_sum[end+1] - acc_sum[start])
    
    return


T = int(input())
for t in range(T):
    K = int(input())
    numbers = list(map(int, input().split()))
    acc_sum = [0] + list(accumulate(numbers))
    dp = [[0]*K for _ in range(K)]
    
    dfs(0, K-1)
    
    print(dp[0][K-1])
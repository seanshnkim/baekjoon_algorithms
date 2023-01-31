import sys

num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    N = int(sys.stdin.readline())
    dp = [[0]*3 for _ in range(N+1)]
    dp[1] = [1, 0, 0]
    dp[2] = [0, 1, 0]
    dp[3] = [1, 1, 1]
    
    for i in range(4, N+1):
        # 더하기 1
        # 더하기 + 2 + 1
        # 더하기 + 3 + 1
        dp[i][0] = dp[i-1][1]% 1000000009 + dp[i-1][2]% 1000000009
        # 더하기 2
        # 더하기 + 1 + 2
        # 더하기 + 3 + 2
        dp[i][1] = dp[i-2][0]% 1000000009 + dp[i-2][2]% 1000000009
        # 더하기 3
        # 더하기 + 1 + 3
        # 더하기 + 2 + 3
        dp[i][2] = dp[i-3][0]% 1000000009 + dp[i-3][1]% 1000000009
    
    print(sum(dp[N]) % 1000000009)
    
    
    
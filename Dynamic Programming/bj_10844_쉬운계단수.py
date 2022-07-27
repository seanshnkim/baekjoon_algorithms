N = int(input())

# dp[N] 은 길이가 N인 계단수에 대한 정보를 담고 있으므로, dp[0]은 0인 리스트로 비워둔다.
dp = [[0 for _ in range(10)] for _ in range(N+1)]

# 끝나는 자릿수대로 dp[n][k] = 길이가 n인 계단수 중 가장 작은 자리의 숫자가 k인 경우의 수
# dp[N][0] + dp[N][1] + ... dp[N][9] = 길이가 N인 계단수의 가짓수
dp[1] = [0] + [1 for _ in range(9)]

if N > 1:
    dp[2][0] = dp[1][1]

    for i in range(1,9):
        dp[2][i] = dp[1][i-1] + dp[1][i+1]
    dp[2][9] = dp[1][8]

if N > 2:
    for n in range(3, N+1):
        dp[n][0] = dp[n-1][1]
        
        for i in range(1,9):
            dp[n][i] = dp[n-1][i-1] + dp[n-1][i+1]
        
        dp[n][9] = dp[n-1][8]

divisor = 1000000000
print(sum(dp[N]) % divisor)
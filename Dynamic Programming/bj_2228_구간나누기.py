import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

dp = [[[0]*N
      for _ in range(N)] 
      for _ in range(M+1)]

dp_max = [[0]*N for _ in range(M+1)]

for i in range(N):
    dp[1][i][i] = numbers[i]
    
for i in range(N):
    for j in range(i+1, N):
        tmp = [0]*(j-i+1)
        tmp[0] = numbers[i]
        
        for k in range(1, j-i+1):
            if tmp[k-1] > 0:
                tmp[k] = tmp[k-1] + numbers[k+i]
            else:
                tmp[k] = numbers[k+i]
        
        dp[1][i][j] = max(tmp)

if M > 1:
    for m in range(2, M+1):
        for i in range(N-1):
            cur = 0
            # 복잡한 코드 -> 이렇게 굳이 경우 안 나눠도 되지 않을까?
            # 이건 다 문제 2번 조건: 서로 다른 두 구간끼리 겹쳐있거나 인접해 있어서는 안 된다.
            # 를 해결하기 위한 것임.
            
            if dp[m][0][i] == dp[m][0][i-1]:
                cur = max(cur, dp[m][0][i-1] + dp[m][i+1][N-1])
            if i < N-2:
                if dp[m][i+1][N-1] == dp[m][i+2][N-1]:
                    cur = max(cur, dp[m][0][i] + dp[m][i+2][N-1])
            
            if (dp[m][0][i] != dp[m][0][i-1]) and \
               (dp[m][i+1][N-1] != dp[m][i+2][N-1]):
                    if i < N -2:
                        cur = max(cur, dp[m][0][i] + dp[m][i+2][N-1])
                    cur = max(dp[m][0][i-1] + dp[m][i+1][N-1])  
            
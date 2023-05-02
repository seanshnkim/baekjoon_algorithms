import sys
input = sys.stdin.readline
from math import ceil

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

dp = [[[-1]*N
      for _ in range(N)] 
      for _ in range(M+1)]

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
    # m == 2인 경우
    cur_max = 0
    for i in range(N-1):
        cur_max = max(cur_max, dp[1][0][i-1] + dp[1][i+1][N-1])
        if i < N-2:
            cur_max = max(cur_max, dp[1][0][i] + dp[1][i+2][N-1])
        
    dp[2][0][N-1] = cur_max

# dp[2][3][N-1]은?

def update_dp(num_I, start, end):
    for i in range(1, num_I):
        cur_max = -1
        for mid in range(start, end):
            # 구간을 num_I-i개, 또는 i개 만들 수 없다는 뜻
            if dp[num_I-i][start][mid] == -1 or dp[i][mid+1][end] == -1:
                continue
            
            # 중간에 비어있다면, 여기선 앞에 것이
            if dp[num_I-i][start][mid] == dp[num_I-i][start][mid-1]:
                cur_max = max(cur_max, \
                          dp[num_I-i][start][mid-1] + dp[num_I-i][mid+1][end])
            if mid < end- 1:
                if dp[num_I-i][mid+1][end] == dp[num_I-i][mid+2][end]:
                    cur_max = max(cur_max, \
                              dp[num_I-i][start][mid] + dp[num_I-i][mid+2][end])
            
            if mid < end - 1:
                if dp[num_I-i][start][mid] != dp[num_I-i][start][mid-1] and \
                    dp[num_I-i][mid+1][end] != dp[num_I-i][mid+2][end]:
                    cur_max = max(cur_max, 
                                  dp[num_I-i][start][mid-1] + dp[num_I-i][mid+1][end], \
                                  dp[num_I-i][start][mid]   + dp[num_I-i][mid+2][end])
            
            else:
                if dp[num_I-i][start][mid] != dp[num_I-i][start][mid-1]:
                    cur_max = max(cur_max, \
                                  dp[num_I-i][start][mid-1] + dp[num_I-i][mid+1][end])
                    
        dp[num_I-i][start][end] = cur_max
    

if M > 1:
    for m in range(2, M+1):
        for s in range(0, N-1):
            for e in range(s+2, N):
                if m > ceil((e-s+1) / 2):
                    continue
                update_dp(m, s, e)

print(dp[M][0][-1])



import sys
input = sys.stdin.readline

N = int(input())
matrices = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
products = [[0]*N for _ in range(N)]

for i in range(N-1):
    products[i][i] = matrices[i][0] * matrices[i][1]
    dp[i][i+1] = products[i][i] * matrices[i+1][1]


for i in range(1, N):
    for j in range(N-i):
        for k in range(i):
            tmp_sum = dp[j][j+k] + dp[j+k+1][j+i] + products[j][j+k] * matrices[j+i][1]
            
            if dp[j][j+i] == 0 or tmp_sum < dp[j][j+i]:
                dp[j][j+i] = tmp_sum
                
            products[j][j+i] = matrices[j][0] * matrices[j+i][1]
            # sum1, mat1_row, mat1_col = dp[j][j+k]
            # sum2, mat2_row, mat2_col = dp[j+k+1][j+i]
            
            # cur_sum = sum1 + sum2 + mat1_row * products[j+k+1][j+i]
            
            # if dp[j][j+i][0] == 0 or cur_sum < dp[j][j+i][0]:
            #     dp[j][j+i] = [cur_sum, matrices[j][0], matrices[j+i][1]]

print(dp[0][-1])
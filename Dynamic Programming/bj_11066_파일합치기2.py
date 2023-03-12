import sys
input = sys.stdin.readline
from itertools import accumulate

# NOTE 
# 이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 
# 소설의 여러 장들이 연속이 되도록 파일을 합쳐나가고!!! 연속!!!
T = int(input())
for t in range(T):
    K = int(input())
    numbers = list(map(int, input().split()))
    dp = [[0]*K for _ in range(K)]
    for i in range(K-1):
        dp[i][i+1] = numbers[i] + numbers[i+1]
    
    acc_sum = [0] + list(accumulate(numbers))
    
    for j in range(2, K):
        for k in range(j-2, -1, -1):
            
            for m in range(k, j):
                if dp[k][j] == 0 or dp[k][j] > dp[k][m] + dp[m+1][j]:
                    dp[k][j] = dp[k][m] + dp[m+1][j]
            
            dp[k][j] += acc_sum[j+1] - acc_sum[k]
            # dp[k][j] += sum(numbers[k+1:j+1])와 동일, but 시간복잡도가 더 클 것

    print(dp[0][-1])
    
'''
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32

dp[0][1] -> 22
dp[1][2] -> 24
dp[2][3] -> 7

0

'''
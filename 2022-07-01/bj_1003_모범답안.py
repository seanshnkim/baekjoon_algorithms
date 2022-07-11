import sys
T = int(input())
dp = [[1,0], [0,1]]
q = [int(sys.stdin.readline()) for _ in range(T)]

# 아예 테스트 케이스에서 
for i in range(2,max(q)+1):
    dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])
for i in q:
    print(dp[i][0], dp[i][1])
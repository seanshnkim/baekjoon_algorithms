import sys
input = sys.stdin.readline

strA = input().rstrip('\n')
lenA = len(strA)
strB = input().rstrip('\n')
lenB = len(strB)

strA = " " + strA
strB = " " + strB
dp = [[0]*(lenB+1) for _ in range(lenA+1)]

for i in range(1, lenA+1):
    for j in range(1, lenB+1):
        if strA[i] == strB[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[lenA][lenB])
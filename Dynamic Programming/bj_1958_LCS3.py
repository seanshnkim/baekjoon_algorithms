import sys
input = sys.stdin.readline

strA = input().rstrip('\n')
strB = input().rstrip('\n')
strC = input().rstrip('\n')
lenA = len(strA)
lenB = len(strB)
lenC = len(strC)

strA = " " + strA
strB = " " + strB
strC = " " + strC

# dp[0~lenA][0~lenB][0~lenC]
dp = [ [[0]*(lenC+1) for _ in range(lenB+1)] for _ in range(lenA+1)]
# subseqAB = [ [[""]*(lenC+1) for _ in range(lenB+1)] for _ in range(lenA+1)]

for i in range(1, lenA+1):
    for j in range(1, lenB+1):
        for k in range(1, lenC+1):
            if strA[i] == strB[j] == strC[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                # subseqAB[i][j][k] = subseqAB[i-1][j-1][k-1] + strA[i]
            else:
                dp[i][j][k] = max(dp[i][j][k-1], dp[i][j-1][k], dp[i-1][j][k])

print(dp[-1][-1][-1])
'''
반례(출처: https://www.acmicpc.net/board/view/6859)
A: dababcf
B: ababdef
C: df

LCS(A,B): ababf
LCS(LCS(A,B),C):  f
LCS(A,B,C): df
'''
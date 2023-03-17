import sys
input = sys.stdin.readline

strA = input().rstrip('\n')
lenA = len(strA)
strB = input().rstrip('\n')
lenB = len(strB)

strA = " " + strA
strB = " " + strB
dp = [[0]*(lenB+1) for _ in range(lenA+1)]
subseq = [[""]*(lenB+1) for _ in range(lenA+1)]

for i in range(1, lenA+1):
    for j in range(1, lenB+1):
        if strA[i] == strB[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            subseq[i][j] = subseq[i-1][j-1] + strA[i]
        else:
            # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                subseq[i][j] = subseq[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                subseq[i][j] = subseq[i][j-1]
            
print(dp[-1][-1])
print(subseq[-1][-1])
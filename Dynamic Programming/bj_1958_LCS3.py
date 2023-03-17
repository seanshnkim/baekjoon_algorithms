import sys
input = sys.stdin.readline

stringA = input().rstrip('\n')
stringB = input().rstrip('\n')
stringC = input().rstrip('\n')

# return the longest common subsequence of strA and strB
def find_LCS(strA, strB):
    lenA = len(strA)
    lenB = len(strB)
    strA = " " + strA
    strB = " " + strB
    dp = [[0]*(lenB+1) for _ in range(lenA+1)]
    subseqAB = [[""]*(lenB+1) for _ in range(lenA+1)]

    for i in range(1, lenA+1):
        for j in range(1, lenB+1):
            if strA[i] == strB[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                subseqAB[i][j] = subseqAB[i-1][j-1] + strA[i]
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                    subseqAB[i][j] = subseqAB[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
                    subseqAB[i][j] = subseqAB[i][j-1]
    
    return subseqAB[-1][-1]

LCS_ABC = find_LCS(stringC, find_LCS(stringA, stringB) )
print(len(LCS_ABC))

'''
반례(출처: https://www.acmicpc.net/board/view/6859)
A: dababcf
B: ababdef
C: df

LCS(A,B): ababf
LCS(LCS(A,B),C):  f
LCS(A,B,C): df
'''
import sys
input = sys.stdin.readline

strA = input().rstrip('\n')
lenA = len(strA)
strB = input().rstrip('\n')
lenB = len(strB)

dp = [[0]*lenB for _ in range(lenA)]

i = lenA-1
j = lenB-1
while True:
    if strA[i] == strB[j]:
        dp[i][j] += 1
        i -= 1
        j -= 1
    else:
        while strB[j] != strA[i]:
            j -= 1
            dp[i][j] = dp[i][j+1]

print(dp[0][0])
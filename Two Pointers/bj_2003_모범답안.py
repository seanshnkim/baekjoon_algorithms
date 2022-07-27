# 2022-07-27(July 27th, 2022), Sehyun Kim

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
firstP = 0
secondP = 1
currSum = arr[firstP]

while firstP < N:
    if currSum == M:
        cnt += 1
        currSum -= arr[firstP]
        firstP += 1
    
    if secondP == N and currSum < M:
        break
    elif currSum < M:
        currSum += arr[secondP]
        secondP += 1
    elif currSum > M:
        currSum -= arr[firstP]
        firstP += 1

print(cnt)
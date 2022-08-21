# 2022-07-27(July 27th), Sehyun Kim

import sys

N = int(input())
numList = list(map(int, sys.stdin.readline().split()))

numList.sort()

# secondP starts from the end of the list
firstP, secondP = 0, N-1
minSum = 2000000000

ans = (numList[firstP], numList[secondP])

while firstP < secondP:
    currSum = abs(numList[firstP] + numList[secondP])
    if currSum < minSum:
        minSum = currSum
        ans = (numList[firstP], numList[secondP])
        secondP -= 1
    elif currSum >= minSum:
        firstP += 1
    
print(*ans)

'''반례:
6
-502 -80 -60 23 100 1002

정답: -80 100 
오답: -80 23'''
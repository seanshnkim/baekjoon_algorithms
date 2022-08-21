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
    currSum = numList[firstP] + numList[secondP]
    if abs(currSum) < minSum:
        minSum = abs(currSum)
        ans = (numList[firstP], numList[secondP])
        if currSum < 0:
            firstP += 1
        elif currSum > 0:
            secondP -= 1
        else:
            break
    elif abs(currSum) >= minSum:
        if currSum < 0:
            firstP += 1
        elif currSum > 0:
            secondP -= 1
        else:
            break
    
print(*ans)


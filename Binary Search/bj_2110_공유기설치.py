import sys
from itertools import accumulate

from numpy import divide

N, C = map(int, input().split())

houseCd = []

for _ in range(N):
    houseCd.append(int(sys.stdin.readline()))

houseCd.sort()
distList = [houseCd[i+1] - houseCd[i] for i in range(N-1)]
sumDist = sum(distList)

def divide_into_maxDist(maxD, nSub):
    i = 0
    cnt_subdivided = 0
    while i < N-1 and cnt_subdivided < nSub:
        subSum = 0
        while subSum < maxD and i < N-1:
            subSum += distList[i]
            i += 1
        if subSum >= maxD:
            cnt_subdivided += 1
    
    return cnt_subdivided


if C == 2:
    print(sumDist)
else:
    maxDist = sumDist // (C-1)
    cnt_subSum = divide_into_maxDist(maxDist, C-1)

    if cnt_subSum == C-1:
        print(maxDist)
    else:
        start = 0
        end = maxDist
        new_maxDist = (start + end) // 2

        cnt_subSum = divide_into_maxDist(new_maxDist, C-1)
        while new_maxDist - start > 1 and end - new_maxDist > 1:
            while cnt_subSum < C-1 and start < end-1:
                maxDist = new_maxDist
                start = 0
                end = maxDist
                new_maxDist = (start + end) // 2
                cnt_subSum = divide_into_maxDist(new_maxDist, C-1)
                
                                
            while cnt_subSum == C-1 and start < end-1:
                start = new_maxDist
                end = maxDist
                new_maxDist = (start + end) // 2
                cnt_subSum = divide_into_maxDist(new_maxDist, C-1)
        
        print(new_maxDist)


        



    


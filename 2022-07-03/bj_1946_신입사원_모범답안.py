# 다시 확인할 것!!!

import sys

nTestCase = int(input())

for t in range(nTestCase):
    nApplic = int(input())
    
    cntRecruit = 1
    people = []

    for i in range(nApplic):
        resumeRank, intervRank = map(int,sys.stdin.readline().split())
        people.append([resumeRank, intervRank])

    people.sort()
    rivalIntervRank = people[0][1]
    
    for i in range(1, nApplic):
        if people[i][1] < rivalIntervRank:
            cntRecruit += 1
            rivalIntervRank = people[i][1]

    print(cntRecruit)

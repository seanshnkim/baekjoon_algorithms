# 2022-07-03, Sehyun Kim
import sys
nTestCase = int(input())

for t in range(nTestCase):
    nApplic = int(input())
    resume_interv = {}

    cntRecruit = nApplic

    for n in range(nApplic):
        resumeRank, intervRank = map(int, sys.stdin.readline().split())
        resume_interv[resumeRank] = intervRank
    
    resume_sorted = sorted(resume_interv.items(), reverse=True)

    spare = 0
    qualifiedRank = 1
    for i, tup in enumerate(resume_sorted):
        if i == nApplic-1: 
            continue
        myIntervRank = tup[1]
        # 탈락
        if myIntervRank > qualifiedRank:
            cntRecruit -=1
        # 합격
        else:
            qualifiedRank += 1
    
    print(cntRecruit)

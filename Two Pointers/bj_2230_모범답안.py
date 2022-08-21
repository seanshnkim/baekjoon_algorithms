# 2022-07-27(July 27th, 2022), Sehyun Kim

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if M > 0:
    # 중복된 아이템은 어차피 minDiff를 구하는 데 영향을 주지 않으므로 set을 이용한다.
    numSet = set()
    for _ in range(N):
        numSet.add(int(input()))

    numList = sorted(list(numSet))

    minDiff = 2000000000
    firstP, secondP = 0, 1
    # maxLen은 N보다 작을 수도 있다
    maxLen = len(numList)
    while secondP < maxLen:
        # currDiff가 반드시 M 이상인 경우가 하나 이상 존재하므로
        if numList[secondP] - numList[firstP] < M:
            secondP += 1
            if secondP == maxLen:
                break
        else:
            # minDiff 업데이트
            minDiff = min(minDiff, numList[secondP] - numList[firstP])
            # firstP 업데이트
            firstP += 1
            # firstP < maxLen 조건도 아래에 포함된다.
            if firstP == secondP:
                secondP += 1
    print(minDiff)

# M == 0일 경우
else:
    print(0)
# 2022-06-27(June 27th, 2022), Sehyun Kim

while(True):
    n = int(input())

    cnt = 1
    currNum = 666
    cntStart = 1
    cntEnd = 10
    zeroCnt = 0

    while(cnt < n):
        isUpdated = 0
        tempNum = currNum
        for i in range(cntStart, cntEnd):
            for j in range(cntEnd):
                frontNum = int(str(i) + '666')
                endNum = int('666' + '0' * zeroCnt + str(j))

                if frontNum > currNum or endNum > currNum:
                    if frontNum > currNum and endNum > currNum:
                        if tempNum < min(frontNum, endNum):
                            ...
                    elif frontNum > currNum:
                        currNum = frontNum
                    elif endNum > currNum:
                        currNum = endNum

                    isUpdated = 1
                    cnt += 1
                    break
                
            if isUpdated:
                break
        if not isUpdated:
            cntStart *= 10
            cntEnd *= 10
            zeroCnt += 1

    print(currNum)


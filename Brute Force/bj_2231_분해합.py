# 2022-06-25(June 25th, 2022), Sehyun Kim

def get_ans(numStr, numInt, lenNum):
    if numInt == 1:
        return 0
    elif numInt <= 18:
        for j in range(1, 18):
            if numInt == j + sum(map(int, str(j))):
                return j
        return 0

    else:
        start = inputInt - 9*lenNum
        end = inputInt - lenNum + 1

        for k in range(start, end):
            if (k + sum(map(int, str(k))) ) == numInt:
                return k
        return 0

inputStr = input()
inputInt = int(inputStr)
inputLen = len(inputStr)

print(get_ans(inputStr, inputInt, inputLen) )
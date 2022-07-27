# 2022-06-25(June 25th, 2022), Sehyun Kim

if __name__ == '__main__':
    numCard, limitSum = map(int, input().split())
    cardNumbers = list(map(int, input().split()))
    cardNumbers.sort()
    numChoice = numCard - 2

    maxSum = 0
    for i in range(numChoice):
        for j in range(i+1, numChoice + 1):
            for k in range(j+1, numChoice + 2):
                currSum  = cardNumbers[i] + cardNumbers[j] + cardNumbers[k]
                if currSum > limitSum:
                    break
                if currSum <= limitSum and currSum > maxSum:
                    maxSum = currSum
    print(maxSum)


    
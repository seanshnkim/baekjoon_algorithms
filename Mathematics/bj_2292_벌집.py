# 2022-06-25(June 25th, 2022), Sehyun Kim

import math

if __name__ == '__main__':
    inputInt = int(input())

    if inputInt == 1:
        print(1)
    elif inputInt <= 4:
        print(2)
    else:
        # TEST 1
        testNum = math.floor(math.sqrt(inputInt / 3))
        lowLimit = 3 * (testNum - 1) * testNum + 2
        uppLimit = 3 * (testNum + 1) * testNum + 1
        if lowLimit <= inputInt <= uppLimit:
            print(testNum + 1)
        else:
            print(testNum + 2)
        

        

        
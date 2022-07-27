import sys

nWine = int(input())
wineList = []
for _ in range(nWine):
    wineList.append(int(sys.stdin.readline()))

if nWine < 3:
    print(sum(wineList))
else:
    sumList = []
    sumList.append([wineList[0], 0])
    sumList.append({0:sumList[0][0], 1:wineList[1], 2:sumList[0][0]+wineList[1]})


    # currDict[0]: chose to skip
    # currDict[1]: chose a wine in this step
    # currDict[2]: chose two wines in a row(last stap and current step), so must skip in the next step
    for n in range(2, nWine):
        currDict = {}
        currDict[0] = max(sumList[n-1][0], sumList[n-1][1], sumList[n-1][2])
        currDict[1] = sumList[n-1][0] + wineList[n]
        currDict[2] = sumList[n-1][1] + wineList[n]

        sumList.append(currDict)

    print(max(sumList[-1].values()))

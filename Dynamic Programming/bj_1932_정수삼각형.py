import sys

nLevel = int(input())
triangle_list = []
sumList = [[0 for _ in range(l+1)] for l in range(nLevel)]

for l in range(nLevel):
    triangle_list.append(list(map(int, sys.stdin.readline().split())))

sumList[0][0] = triangle_list[0][0]

for lv in range(1, nLevel):
    sumList[lv][0] = sumList[lv-1][0] + triangle_list[lv][0]
    
    for l in range(lv-1):
        sumList[lv][l+1] = max(sumList[lv-1][l], sumList[lv-1][l+1]) + triangle_list[lv][l+1]
    
    sumList[lv][lv] = sumList[lv-1][lv-1] + triangle_list[lv][lv]

print(max(sumList[-1]))

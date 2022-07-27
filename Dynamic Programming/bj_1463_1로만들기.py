# 2022-06-25(June 25th, 2022), Sehyun Kim

saveCnt  = [0]
n = int(input())

for k in range(2, n+1):
    saveCnt.append(saveCnt[k-2] + 1)
    if k % 2 == 0:
        saveCnt[k-1] = min(saveCnt[k-1], saveCnt[k//2 - 1] + 1)
    if k % 3 == 0:
        saveCnt[k-1] = min(saveCnt[k-1], saveCnt[k//3 - 1] + 1)

print(saveCnt[-1])



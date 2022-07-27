numTestCase = int(input())

nList = []
for t in range(numTestCase):
    nList.append(int(input()))

maxNum = max(nList)

dp_table = [0 for i in range(11)]
dp_table[1] = 1
dp_table[2] = 2
dp_table[3] = 4

if maxNum > 3:
    for i in range(4, maxNum+1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2] + dp_table[i-3]

for num in nList:
    print(dp_table[num])

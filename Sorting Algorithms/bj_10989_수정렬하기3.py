# 2022-06-27(June 27th, 2022), Sehyun Kim

# counting 정렬
import sys

n = int(input())
cntArr = [0] * 10001

# input을 받아옴과 동시에 배열에 값을 저장하므로 for loop을 2번 실행할 필요가 없다.
for i in range(n):
    inputInt = int(sys.stdin.readline())
    cntArr[inputInt] += 1

for c in range(10001):
    currCnt = cntArr[c]
    if currCnt > 0:
        for i in range(currCnt):
            print(c)
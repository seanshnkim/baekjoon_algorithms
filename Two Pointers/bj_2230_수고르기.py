# 2022-07-27(July 27th, 2022), Sehyun Kim

import sys

N, M = map(int, sys.stdin.readline().split())
numList = []

for _ in range(N):
    numList.append(int(sys.stdin.readline()))

firstP = 0
secondP = 1
currDiff = 0
minDiff = 2000000000

# 아, 먼저 sort를 했어야 했구나...(30분동안 헤매다 깨달음)
numList.sort()

while firstP < N:
    if currDiff >= M:
        if currDiff < minDiff:
            minDiff = currDiff
        
        currDiff += numList[firstP]
        firstP += 1
        # firstP < N 이거 안 붙이면 indexError 발생
        if firstP < N:
            currDiff -= numList[firstP]
    
    # 그냥 if 가 아니라 elif 이어야 한다. indexError가 발생할 수도 있다.
    elif currDiff < M and secondP < N:
    # if currDiff < M and currDiff >= minDiff and secondP < N:
    # if currDiff < M and currDiff < minDiff and secondP < N: 도 마찬가지다.
    # currDiff < M 이므로 계속 currDiff를 증가시켜야 한다
        currDiff = (numList[secondP] - numList[firstP])
        secondP += 1
    
    # 더 이상 firstP를 증가시켜봤자 currDiff는 계속 감소할 것이고, 루프를 계속 돌 이유가 없다.
    # 그리고 문제 조건에 따라 minDiff >= M는 자명하므로 확인할 필요가 없다
    # N = 1일 경우, M = 0만 가능하며 초기 currDiff = 0이므로 currDiff <(미만) M 으로 설정하면 안됨
    # currDiff < M이라고 조건 걸어도 되기는 하는데 그럼 currDiff == M 일 때 계속 쓸데없이 firstP를 증가시켜서 끝까지 증가시킨 다음에야 종료할 것...
    elif currDiff <= M and secondP == N:
        # 2번째 반례를 주석에 메모해둘 것
        # if currDiff < minDiff:
        #     minDiff = currDiff
        break
    
    # if currDiff < M and currDiff >= minDiff and secondP == N:
        # 일어날 수 없는 일 (항상 차이가 M 이상인 두 수를 고를 수 있다고 했으므로)
    
    # if currDiff < M and currDiff < minDiff and secondP == N:
        # 일어날 수 없는 일
    
print(minDiff)

'''2번째 반례:
8 10
1
2
3
4
5
6
7
16
'''
# 2022-07-27(July 27th, 2022), Sehyun Kim
import sys

N, M = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))

firstP = 0
secondP = 0
cnt = 0
currSum = numList[0]

# 틀렸던 이유!!!!
# while secondP < N:

# 이렇게 하면 또 시간 초과가 뜬다
# while firstP < N:
#     currSum = 0
#     secondP = firstP
#     # secondP < M 조건을 inner loop에 한번 더 써야한다는 게 바람직하지 않다. 다른 방법이 있을까?
#     while (currSum < M and secondP < N):
#         currSum += numList[secondP]
#         secondP += 1
#     if currSum == M:
#         cnt += 1
#     firstP += 1

# 결국 모범답안대로 해야 한다.
while firstP < N:
    if currSum == M:
        cnt += 1
        currSum -= numList[firstP]
        firstP += 1
    
    if secondP == N and currSum < M:
        break
    elif currSum < M:
        currSum += numList[secondP]
        secondP += 1
    elif currSum > M:
        currSum -= numList[firstP]
        firstP += 1

print(cnt)

# 오늘의 교훈 1) 잠을 충분히 자자
# 2) 처음부터 끝까지 다 디버깅을 해보고 코드를 짜자.

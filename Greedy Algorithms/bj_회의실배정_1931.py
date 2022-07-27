# 2022-07-03, Sehyun Kim
n = int(input())

listStartEnd = []
for _ in range(n):
    start, end = map(int, input().split())
    # append takes exactly one argument -> 괄호 쳐야 함
    listStartEnd.append((start, end))

# key(시작 시간)를 기준으로 정렬
sortedList = sorted(listStartEnd, reverse=True)
cnt = 1

# 시작 시간이 가장 늦은 녀석을 시작으로
currStart = sortedList[0][0]
for i in range(1, n):
    currEnd = sortedList[i][1]
    if currEnd <= currStart:
        # 어차피 start 시작 시간이 정렬되어 있는 리스트이므로.
        currStart = sortedList[i][0]
        cnt += 1

print(cnt)
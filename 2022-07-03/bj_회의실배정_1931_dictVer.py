n = int(input())

listStartEnd = []
for _ in range(n):
    start, end = map(int, input().split())
    # append takes exactly one argument -> 괄호 쳐야 함
    listStartEnd.append((end, start))

# key(시작 시간)를 기준으로 정렬
sortedList = sorted(listStartEnd)
cnt = 0

currEnd = 0
for e, s in sortedList:
    if currEnd <= s:
        currEnd = e
        cnt += 1

print(cnt)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0
i = 0
cur_set = set()
while cnt < N:
    cur_num = numbers[i]
    if cur_num not in cur_set:
        cur_set.add(cur_num)
        cnt += 1
    i += 1

ans = 0
while i < K:
    cur_num = numbers[i]
    if cur_num not in cur_set:
        # cur_set의 어떤 원소를 제거해야 할까?
        ...
        ans += 1
    i += 1
    
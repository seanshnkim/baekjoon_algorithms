import sys
input = sys.stdin.readline
from collections import Counter

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
num_cnts = Counter(numbers)

cnt = 0
i = 0
cur_set = set()
while cnt < N:
    cur_num = numbers[i]
    if cur_num not in cur_set:
        cur_set.add(cur_num)
        cnt += 1
    num_cnts[cur_num] -= 1
    i += 1


while i < K:
    cur_num = numbers[i]
    if cur_num not in cur_set:
        # num_cnts 개수가 제일 적은 것부터 삭제
        ...
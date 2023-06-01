import sys
input = sys.stdin.readline
from collections import Counter

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
num_cnts = Counter(numbers)

cnt_device = 0
i = 0
set_outlet = set()
while cnt_device < N:
    cur_num = numbers[i]
    if cur_num not in set_outlet:
        set_outlet.add(cur_num)
        cnt_device += 1
    num_cnts[cur_num] -= 1
    i += 1


def remove_outlet(input_set, cur_idx):
    for s in input_set:
        # 아예 미래에 등장할 일이 없는 플러그 제거
        if num_cnts[s] == 0:
            input_set.remove(s)
            return
    
    max_idx = -1
    for s in input_set:
        max_idx = max(numbers[cur_idx:].index(s)+cur_idx, max_idx)
    
    if max_idx != -1:
        input_set.remove(numbers[max_idx])
    return


ans = 0 
while i < K:
    cur_num = numbers[i]
    if cur_num not in set_outlet:
        remove_outlet(set_outlet, i)
        ans += 1
        set_outlet.add(cur_num)
    
    num_cnts[cur_num] -= 1
    i += 1

print(ans)
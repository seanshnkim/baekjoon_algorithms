# 2022-08-06(August 6th, 2022), Sehyun Kim

import sys

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
num_list = [0] + num_list 
max_list = [0] + [num_list[0]] + [0] * (N-1)

for num_card in range(1, N+1):
    half_num = num_card // 2
    curr_max = num_list[num_card]
    for k in range(1, half_num+1):
        curr_max = max(max_list[num_card-k] + max_list[k], curr_max)
    max_list[num_card] = curr_max

print(max_list[N])

import sys
input = sys.stdin.readline
from collections import defaultdict

N, C = map(int, input().split())
numbers = list(map(int, input().split()))
mid = N // 2

left_sums = defaultdict(int)
for bit_mask in range(1 << mid):
    cur_sum = 0
    for k in range(mid):
        if bit_mask & (1<<k) != 0:
            cur_sum += numbers[k]
    if cur_sum <= C:
        left_sums[cur_sum] += 1

ans = 0
right_sums = defaultdict(int)
for bit_mask in range(1 << (N-mid)):
    cur_sum = 0
    for k in range(N-mid):
        if bit_mask & (1<<k) != 0:
            cur_sum += numbers[mid+k]
    if cur_sum <= C:
        right_sums[cur_sum] += 1

ans = 0
for sum_w in range(C+1):
    for w in range(sum_w+1):
        ans += left_sums[w] * right_sums[sum_w - w]

print(ans)
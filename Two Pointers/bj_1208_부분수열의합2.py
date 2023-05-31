import sys
input = sys.stdin.readline
from collections import defaultdict

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

mid = N // 2

left_sums = defaultdict(int)
for bit_mask in range(1 << mid):
    cur_sum = 0
    for k in range(mid):
        if bit_mask & (1<<k) != 0:
            cur_sum += numbers[k]
    left_sums[cur_sum] += 1
    
ans = 0

for bit_mask in range(1 << (N-mid)):
    cur_sum = 0
    for k in range(N-mid):
        if bit_mask & (1<<k) != 0:
            cur_sum += numbers[mid+k]
    if (S - cur_sum) in left_sums.keys():
        ans += left_sums[S-cur_sum]

# 그리고 맨 마지막엔, 아무 것도 선택하지 않은 경우는 빼주어야 함
if S == 0:
    print(ans-1)
else:
    print(ans)
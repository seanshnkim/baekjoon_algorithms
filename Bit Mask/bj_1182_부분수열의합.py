import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

cnt = 0
for bit_mask in range(1, 1<<N):
    sum = 0
    for k in range(N):
        if bit_mask & (1<<k) != 0:
            sum += nums[k]
    if sum == S:
        cnt += 1

print(cnt)
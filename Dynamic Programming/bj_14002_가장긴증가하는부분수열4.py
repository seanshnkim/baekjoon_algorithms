import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

lengths = [0 for _ in range(N)]
LIS = [[] for _ in range(N)]

for i in range(N):
    for prev_idx in range(i-1, -1, -1):
        if nums[i] > nums[prev_idx]:
            if lengths[prev_idx] + 1 > lengths[i]:
                lengths[i] = lengths[prev_idx] + 1
                LIS[i] = LIS[prev_idx] + [nums[i]]
    if lengths[i] == 0:
        lengths[i] = 1
        LIS[i] = [nums[i]]

max_len = 0
max_idx = 0
for i in range(N):
    if lengths[i] > max_len:
        max_len = lengths[i]
        max_idx = i

print(max_len)
print(*LIS[max_idx])
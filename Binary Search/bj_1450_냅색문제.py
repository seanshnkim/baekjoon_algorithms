import sys
input = sys.stdin.readline

N, C = map(int, input().split())
numbers = list(map(int, input().split()))
half = N // 2

# left_sums = defaultdict(int)
left_sums = []
for bit_mask in range(1 << half):
    cur_sum = 0
    for k in range(half):
        if cur_sum > C:
            break
        if bit_mask & (1<<k) != 0:
            cur_sum += numbers[k]
    if cur_sum <= C:
        left_sums.append(cur_sum)
    # if cur_sum <= C:
    #     left_sums[cur_sum] += 1

ans = 0
# right_sums = defaultdict(int)
right_sums = []
for bit_mask in range(1 << (N-half)):
    cur_sum = 0
    for k in range(N-half):
        if cur_sum > C:
            break
        if bit_mask & (1<<k) != 0:
            cur_sum += numbers[half+k]
    if cur_sum <= C:
        right_sums.append(cur_sum)
#     if cur_sum <= C:
#         for S in range(C - cur_sum + 1):
#             if S in left_sums.keys():
#                 ans += left_sums[S]

right_sums.sort()
for s in left_sums:
    start, end = 0, len(right_sums)
    while start < end:
        mid = (start + end) // 2
        if right_sums[mid] <= C-s:
            start = mid+1
        else:
            end = mid
    ans += start

print(ans)
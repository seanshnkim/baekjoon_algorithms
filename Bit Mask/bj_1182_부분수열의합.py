import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(1, 1<<N):
    i_expanded = [((1<<k) & i) >> k for k in range(N-1, -1, -1)]
    if sum(m*n for m,n in zip(nums, i_expanded) ) == S:
        cnt += 1

print(cnt)
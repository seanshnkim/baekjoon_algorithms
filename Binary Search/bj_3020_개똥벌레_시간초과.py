# 2022-08-07(August 7th), Sehyun Kim
import sys
input = sys.stdin.readline

n, H = map(int, input().split())

down = [0] * (H + 1)
up = [0] * (H + 1)

# Starts from the maximum number of obstacles, n
min_obs = n
min_obs_cnt = 0

for i in range(n):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in reversed(range(0, H)):
    down[i] += down[i + 1]
    up[i] += up[i + 1]

for i in range(1, H+1):
    curr_obs = down[i] + up[H-i+1]
    if curr_obs < min_obs:
        min_obs = curr_obs
        min_obs_cnt = 1
    elif min_obs == curr_obs:
        min_obs_cnt += 1

print(min_obs, min_obs_cnt)
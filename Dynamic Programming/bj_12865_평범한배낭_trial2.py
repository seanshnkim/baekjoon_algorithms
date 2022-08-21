# 2022-08-06(August 6th, 2022), Sehyun Kim
# 시간 7428ms -> 느리다!

import sys

N, W = map(int, sys.stdin.readline().split())

w_list = [0] 
v_list = [0]
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]


for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    w_list.append(weight)
    v_list.append(value)

for n in range(1, N+1):
    for w in range(1, W+1):
        if w >= w_list[n]:
            dp[n][w] = max(dp[n-1][w], dp[n-1][w - w_list[n]] + v_list[n])
        else:
            dp[n][w] = dp[n-1][w]

print(dp[N][W])

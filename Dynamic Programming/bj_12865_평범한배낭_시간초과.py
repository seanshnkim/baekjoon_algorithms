import sys

N, max_W = map(int, sys.stdin.readline().split())

wv_list = [] 
dp = [-1] * (max_W+1)
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    wv_list.append((weight, value))
    dp[weight] = value

wv_list_sorted = sorted(wv_list)

# curr_w starts from minimum weight
min_w = wv_list_sorted[0][0]

for w in range(min_w, max_W+1):
    half_w = w // 2
    curr_max = max(dp[:w+1])
    for k in range(1, half_w + 1):
        if dp[w-k] != -1 and dp[k] != -1:
            curr_max = max(dp[w-k] + dp[k], curr_max)
        dp[w] = curr_max

print(dp[max_W])

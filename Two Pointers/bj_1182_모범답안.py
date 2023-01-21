import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

cnt = 0

def dfs(idx, curr_sum):
    global cnt
    
    if idx >= N:
        return

    if curr_sum == S:
        cnt += 1
    
    dfs(idx+1, curr_sum)
    dfs(idx+1, curr_sum + nums[idx])

dfs(0,0)
print(cnt)
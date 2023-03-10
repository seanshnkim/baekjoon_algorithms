import sys
input = sys.stdin.readline

N, START, LIMIT = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [set() for _ in range(N+1)]
dp[0].add(START)

def solution():
    for i in range(N):
        if not dp[i]:
            return -1
        
        cur_list = list(dp[i])
        for prev in cur_list:
            cur_vol = prev + volumes[i]
            if cur_vol <= LIMIT:
                dp[i+1].add(cur_vol)
            
            cur_vol = prev - volumes[i]
            if 0 <= cur_vol:
                dp[i+1].add(cur_vol)
            
    if dp[-1]:
        return max(list(dp[-1]))
    else:
        return -1

print(solution())
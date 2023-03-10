import sys
input = sys.stdin.readline

N, START, LIMIT = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [[] for _ in range(N+1)]
dp[0] = [START]

def solution():
    for i in range(N):
        if not dp[i]:
            return -1
        
        for prev in dp[i]:
            cur_vol = prev + volumes[i]
            if cur_vol <= LIMIT:
                dp[i+1].append(cur_vol)
            
            cur_vol = prev - volumes[i]
            if 0 <= cur_vol:
                dp[i+1].append(cur_vol)
            
    if dp[-1]:
        return max(dp[-1])
    else:
        return -1

print(solution())

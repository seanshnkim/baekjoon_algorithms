import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def digits(n):
    i = 0
    tmp = n
    while tmp >= 10:
        tmp = tmp // 10
        i += 1
    
    cnt = 0
    k = n
    while k > 0:
        cnt += (k-(10**i-1)) * (i+1)
        k = (10**i-1)
        i -= 1
        
    return cnt


def solution(targ, left, right):
    
    mid = (left+right) // 2
    
    while left <= right:
        mid_digits = digits(mid)
        if mid_digits > targ:
            return solution(targ, left, mid-1)
        elif mid_digits < targ:
            return solution(targ, mid+1, right)
        else:
            return str(mid)[-1]
    
    curr = max(left, right)
    steps = targ - digits(curr)
    
    return str(curr)[steps-1]


if digits(N) < K:
    print(-1)
else:
    print(solution(K, 1, N))
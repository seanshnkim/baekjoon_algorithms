import sys
input = sys.stdin.readline

N, n_targ = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()


def how_many(l):
    cnt = 0
    for n in nums:
        cnt += (n // l)
    return cnt


def solution(targ_num, left, right):
    mid = (left + right) // 2
    
    while left <= right:
        if how_many(mid) > targ_num:
            solution(targ_num, left, mid-1)
        elif how_many(mid) < targ_num:
            solution(targ_num, mid+1, right)
        else:
            return mid
    return mid
    


# WRONG
# print(solution(0, N-1))
min_len, max_len = 0, nums[-1]
print(solution(n_targ, min_len, max_len))
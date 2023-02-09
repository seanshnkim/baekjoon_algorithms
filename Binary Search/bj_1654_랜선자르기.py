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
            #FIXME - 거꾸로! -> 몫을 구하는 연산이기 때문에,
            # 현재 값이 targ_num보다 크다는 건 그만큼 길이(나눠주는 길이)가 작다는 것
            # solution(targ_num, left, mid-1)
            return solution(targ_num, mid+1, right)
        elif how_many(mid) < targ_num:
            # solution(targ_num, mid+1, right)
            return solution(targ_num, left, mid-1)
        else:
            return mid
    return mid
    


# WRONG
# print(solution(0, N-1))
min_len, max_len = 0, nums[-1]
print(solution(n_targ, min_len, max_len))
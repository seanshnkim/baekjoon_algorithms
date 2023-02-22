import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
# 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)
cnt_operators = list(map(int, input().split()))
idx_operators = []
for i in range(4):
    idx_operators.extend([i for _ in range(cnt_operators[i])])
    
max_result = -10**9
min_result = 10**9

curr_permutations = permutations(idx_operators)
checked = []

for permut in curr_permutations:
    res = nums[0]
    for n in range(1, N):
        if permut[n-1] == 0:
            res += nums[n]
        elif permut[n-1] == 1:
            res -= nums[n]
        elif permut[n-1] == 2:
            res *= nums[n]
        else:
            if res < 0:
                res = -(-res // nums[n])
            else:
                res //= nums[n]
    
    max_result = max(max_result, res)
    min_result = min(min_result, res)

print(max_result)
print(min_result)

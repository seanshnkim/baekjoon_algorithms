# 왜 이 문제를 이렇게 헤맸을까?

import sys
input = sys.stdin.readline

N = int(input())
printed_nums = [int(input().rstrip('\n')) for _ in range(N)]

stack = []
answer = []
is_stack_sequence = True

top = 0
for i in range(N):
    curr_num = printed_nums[i]
    if curr_num > top:
        for i in range(top+1, curr_num+1):
            stack.append(i)
            answer.append('+')
        top = curr_num
    
    popped = stack.pop()
    answer.append('-')
    
    if popped != curr_num:
        is_stack_sequence = False
        break


if not is_stack_sequence:
    print("NO")
else:
    print(*answer, sep='\n')
import sys

n_sym = int(sys.stdin.readline())
syms = list(sys.stdin.readline().split())
complete_nums = []

def is_next(idx, curr_str, n):
    if (syms[idx] == '>' and curr_str[-1] > str(n)) or \
       (syms[idx] == '<' and curr_str[-1] < str(n)):
        return True
    return False
    

def solution(idx, curr_str):
    if idx == n_sym:
        complete_nums.append(curr_str)
        return
    for n in range(10):
        if str(n) not in curr_str and is_next(idx, curr_str, n):
            solution(idx+1, curr_str+str(n))
    return

for i in range(10):
    solution(0, str(i))
print(max(complete_nums))
print(min(complete_nums))
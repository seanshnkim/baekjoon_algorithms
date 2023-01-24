import sys

n_signs = int(sys.stdin.readline())
signs = list(sys.stdin.readline().split())
used = [False for _ in range(10)]
answers = []

def is_next(x, y, op):
    if op == '<':
        if x > y:
            return False
    if op == '>':
        if x < y:
            return False
    return True


def solution(idx, n_str_list):
    if idx == n_signs+1:
        answers.append(n_str_list)
        return
    
    for i in range(10):
        if used[i]:
            continue
        if idx == 0 or is_next(n_str_list[idx-1], str(i), signs[idx-1]):
            used[i] = True
            solution(idx+1, n_str_list+str(i))
            used[i] = False

solution(0, '')
print(max(answers))
print(min(answers))

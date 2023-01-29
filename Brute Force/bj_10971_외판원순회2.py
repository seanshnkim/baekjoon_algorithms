import sys

N = int(sys.stdin.readline())
W_matrix = []
answers = []
for _ in range(N):
    W_matrix.append(list(map(int, sys.stdin.readline().split())))


def solution(curr_path, curr_W_sum):
    if len(curr_path) == N:
        curr_W_sum += W_matrix[curr_path[-1]][curr_path[0]]
        answers.append(curr_W_sum)
        return
    
    
    max_W = curr_W_sum
    for i in range(N):
        if i in curr_path:
            continue
        if not curr_path:
            solution([i], 0)
        else:
            solution(curr_path+[i], curr_W_sum + W_matrix[curr_path[-1]][i])
    return 


solution([], 0)
print(min(answers))

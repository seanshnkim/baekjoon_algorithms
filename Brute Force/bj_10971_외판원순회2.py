import sys

N = int(sys.stdin.readline())
W_matrix = []
answers = []
for _ in range(N):
    W_matrix.append(list(map(int, sys.stdin.readline().split())))


def solution(curr_path, curr_W_sum):
    # 돌아오는 것도 가능해야 한다!
    if len(curr_path) == N:
        curr_weight = W_matrix[curr_path[-1]][curr_path[0]]
        if curr_weight > 0:
            answers.append(curr_W_sum + curr_weight)
        return
    
    for i in range(1, N):
        if i in curr_path:
            continue
        curr_weight = W_matrix[curr_path[-1]][i]
        if curr_weight > 0:
            solution(curr_path+[i], curr_W_sum+curr_weight)
    return 


solution([0], 0)
print(min(answers))
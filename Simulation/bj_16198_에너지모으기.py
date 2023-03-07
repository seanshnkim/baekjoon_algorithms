import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))


def solution(weight):
    len_weight = len(weight)
    if len_weight == 3:
        return weight[0]*weight[-1]
    
    answer = 0
    for i in range(1, len_weight-1):
        cur_energy = weight[i-1]*weight[i+1]
        prev_w = weight[i]
        weight.pop(i)
        answer = max(answer, solution(weight)+cur_energy)
        weight.insert(i, prev_w)
    
    return answer

print(solution(weights))
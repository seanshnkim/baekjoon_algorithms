import sys

N = int(sys.stdin.readline())

arr_2D = []

for _ in range(N):
    arr_2D.append(list(map(int, sys.stdin.readline().split())))


def sums(new, teamA, teamB):
    sumA = sumB = 0
    
    for a,b in zip(teamA, teamB):
        sumA += (arr_2D[a][new] + arr_2D[new][a])
        sumB += (arr_2D[b][new] + arr_2D[new][b])
    
    return sumA, sumB


def solution(idx, teamA, teamB, sumA, sumB):
    global min_diff
    
    if len(teamA) > N//2 or len(teamB) > N//2:
        return float('inf')
    
    # if len(teamA) == N//2 and len(teamB) == N//2:
    #     return abs( (sumA+new_sumA) - (sumB+new_sumB) )
    if len(teamA) == N//2 and len(teamB) == N//2:
        min_diff = min(min_diff, abs(sumA - sumB))
    
    if idx == N:
        return float('inf')
    
    new_sumA, new_sumB= sums(idx, teamA, teamB)
    
    for i in range(idx, N):
        min_diff = min(solution(i+1, teamA+[i], teamB, sumA+new_sumA, sumB), \
                       solution(i+1, teamA, teamB+[i], sumA, sumB+new_sumB))
    
    return min_diff

min_diff = float('inf')
print(solution(0, [], [], 0, 0))
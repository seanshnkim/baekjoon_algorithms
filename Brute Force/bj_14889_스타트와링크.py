import sys

N = int(sys.stdin.readline())

arr_2D = []

for _ in range(N):
    arr_2D.append(list(map(int, sys.stdin.readline().split())))


def diff_sums(teamA, teamB):
    sumA = sumB = 0
    
    for i in range(N//2):
        for j in range(N//2):
            if i == j:
                continue
            sumA += arr_2D[teamA[i]][teamA[j]] + arr_2D[teamA[j]][teamA[i]]
            sumB += arr_2D[teamB[i]][teamB[j]] + arr_2D[teamB[j]][teamB[i]]
    
    return abs(sumA - sumB)


def solution(idx, teamA, teamB):
    
    if len(teamA) > N//2 or len(teamB) > N//2:
        return -1
    
    # if len(teamA) == N//2 and len(teamB) == N//2:
    #     return abs( (sumA+new_sumA) - (sumB+new_sumB) )
    if len(teamA) == N//2 and len(teamB) == N//2:
        return diff_sums(teamA, teamB)
    
    if idx == N:
        return -1
    
    t1 = solution(idx+1, teamA+[idx+1], teamB)
    t2 = solution(idx+1, teamA, teamB+[idx+1])
    
    # min_diff는 -1이 나올 수도 있다.
    min_diff = -1
    if t1 != -1 and t2 != -1:
        min_diff = min(t1, t2)
    return min_diff

# print(solution(0, [], []))
print(solution(-1, [], []))
import sys

N = int(sys.stdin.readline())

arr_2D = []

for _ in range(N):
    arr_2D.append(list(map(int, sys.stdin.readline().split())))


def diff_sums(teamA, teamB):
    sumA = sumB = 0
    
    for i in range(N//2):
        for j in range(i+1, N//2):
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
    
    min_diff = -1
    # min_diff가 -1 값을 그대로 유지한 채 나올 수 있다.
    '''
    A = solution(idx+1, teamA+[idx+1], teamB)
    tB = solution(idx+1, teamA, teamB+[idx+1])
    if tA != -1 and tB != -1:
        min_diff = min(tA, tB)
    return min_diff
    '''
    # 아래와 같이 min_diff == -1이면 반드시 업데이트를 하도록 if문 조건에 추가해줘야 함
    tA = solution(idx+1, teamA+[idx+1], teamB)
    if min_diff == -1 or (tA != -1 and min_diff > tA):
        min_diff = tA
    tB = solution(idx+1, teamA, teamB+[idx+1])
    if min_diff == -1 or (tB != -1 and min_diff > tB):
        min_diff = tB
    
    return min_diff

# print(solution(0, [], []))
print(solution(-1, [], []))
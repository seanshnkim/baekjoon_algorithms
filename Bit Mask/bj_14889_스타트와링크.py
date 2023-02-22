import sys
input = sys.stdin.readline

from itertools import combinations

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 좀 다른 풀이
# from itertools import combinations

# combinations_N = combinations(range(N), N//2)

# for curr_comb in combinations_N:
#     teamA = 0
#     teamB = 0
#     pair_comb = combinations(curr_comb, 2)
#     for pair in pair_comb:
#         i, j = pair
#         teamA += (board[i][j] + board[j][i])
teamA = []
teamB = []
min_diff = float('inf')
for i in range(1<<(N//2-1)):
    toggled = i ^ ((1<< N//2) - 1)
    state = (toggled << (N//2)) + i
    
    teamA = []
    teamA_sum = 0
    teamB = []
    teamB_sum = 0
    
    for j in range(N):
        if state & (1<<j) != 0:
            teamA.append(j)
        else:
            teamB.append(j)
    
    pairs_teamA= combinations(teamA, 2)
    pairs_teamB= combinations(teamB, 2)
    for pair in pairs_teamA:
        m1, m2 = pair
        teamA_sum += (board[m1][m2] + board[m2][m1])
    for pair in pairs_teamB:
        m1, m2 = pair
        teamB_sum += (board[m1][m2] + board[m2][m1])
    
    min_diff = min(min_diff, abs(teamA_sum - teamB_sum))

print(min_diff)
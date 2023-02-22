import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')

for i in range(1<<N):
    cnt_teamA = 0
    teamA_idx = []
    teamB_idx = []
    teamA_sum = 0
    teamB_sum = 0
    
    for j in range(N):
        if i & (1<<j) != 0:
            cnt_teamA += 1
            teamA_idx.append(j)
        else:
            teamB_idx.append(j)
    
    if cnt_teamA == N//2:
        for k in range(N//2):
            for l in range(k+1, N//2):
                m1_idx = teamA_idx[k]
                m2_idx = teamA_idx[l]
                teamA_sum += board[m1_idx][m2_idx] + board[m2_idx][m1_idx]
        
        for k in range(N//2):
            for l in range(k+1, N//2):
                m1_idx = teamB_idx[k]
                m2_idx = teamB_idx[l]
                teamB_sum += board[m1_idx][m2_idx] + board[m2_idx][m1_idx]
        
        answer = min(answer, abs(teamA_sum - teamB_sum))

print(answer)
import sys
input = sys.stdin.readline
from itertools import combinations

N, n_virus = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N) ]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

virus_loc = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            virus_loc.append( (r, c) )
            

def in_board(x, y):
    return 0 <= x < N and 0 <= y < N


def proliferate(board, activated_virus):
    cur_activated = []
    for virus in activated_virus:
        x, y = virus
        
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            if in_board(mx, my):
                if board[mx][my] == 0 or board[mx][my] == 2:
                    # 활성 상태의 바이러스가 빈칸에 복제되면 활성상태의 바이러스가 되는 거 맞나?
                    board[mx][my] = 3
                    cur_activated.append((mx, my))
                    # 여기서 다시 board[mx][my] == 0을 해주어야 할까?
    
    activated_virus.extend(cur_activated)
    return activated_virus


def empty_cells(board):
    cnt = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                cnt += 1
    return cnt
    

answer = 0
for comb in combinations(virus_loc, n_virus):
    # 활성이면 2에서 1을 더해서 3으로 표시하기로 하자(따라서, 여전히 비활성이면 2이다).
    tmp_board = [row.copy() for row in board]
    # 그리고 고른 위치 M개(comb)에 대해 활성화 상태로 만들어주어야 함
    for x,y in comb:
        tmp_board[x][y] = 3
    
    # cnt_empty = sum(sum(1 if item == 0 else 0 for item in board[r]) \
    #                     for r in range(N))
    cnt_empty = 0
    cnt_time = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                cnt_empty += 1
    
    act_virus = list(comb)
    while cnt_empty > 0:
        new_act = proliferate(tmp_board, act_virus)
        cur_empty = empty_cells(tmp_board)
        # 즉 이전 cnt와 현재 cnt가 같고, 빈칸이 줄어들지 않는다는 건 더 이상 바이러스를 퍼뜨릴 수 없다는 뜻
        if cnt_empty == cur_empty:
            answer = -1
            break
        else:
            cnt_empty = cur_empty
            act_virus = new_act
            cnt_time += 1
    
    if answer == -1:
        break
    elif answer == 0 or answer > cnt_time:
        answer = cnt_time

print(answer)
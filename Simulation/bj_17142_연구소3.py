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
    cnt_no_empty = 0
    for virus in activated_virus:
        x, y = virus
        
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            if in_board(mx, my):
                if board[mx][my] == 0 or board[mx][my] == 2:
                    if board[mx][my] == 0:
                        cnt_no_empty += 1
                    board[mx][my] = 3
                    cur_activated.append((mx, my))
    
    return cur_activated, cnt_no_empty


# def count_empty(board):
#     cnt = 0
#     for r in range(N):
#         for c in range(N):
#             if board[r][c] == 0:
#                 cnt += 1
#     return cnt
    

answers = []
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
        new_act, cnt_no_empty = proliferate(tmp_board, act_virus)
        cnt_empty -= cnt_no_empty
        # 즉 이전 cnt와 현재 cnt가 같고, 빈칸이 줄어들지 않는다는 건 더 이상 바이러스를 퍼뜨릴 수 없다는 뜻
        # 더 이상 증식할 수 없다면(activated_cell 개수가 증가X) 멈추는 걸로 판정하자.
        # if cnt_empty == cur_empty:
        if new_act:
            act_virus.extend(new_act)
            cnt_time += 1
        else:
            cnt_time = -1
            break
    
    # FIXME - 그리고 수많은 조합 경우의 수 중에 도달할 수 없는 경우도 있고, 도달할 수 있는 경우도 있을 것
    answers.append(cnt_time)

# cur_ans = answers[0]
# for ans in answers:
#     if (cur_ans == -1 and ans != -1) or ans < cur_ans:
#         cur_ans = ans
valid_answers = [ans for ans in answers if ans != - 1]
if valid_answers:
    print(min(valid_answers))
else:
    print(-1)
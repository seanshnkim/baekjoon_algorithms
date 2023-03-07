import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

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


def bfs(start, count_empty):
    cnt_empty = count_empty
    q = deque()
    visited = [[-1]*N for _ in range(N)]
    for x,y in start:
        q.append((x,y))
        visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        if cnt_empty == 0:
            break
        
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            if in_board(mx, my) and visited[mx][my] == -1:
                if board[mx][my] == 0 or board[mx][my] == 2:
                    if board[mx][my] == 0:
                        cnt_empty -= 1
                    q.append((mx, my))
                    visited[mx][my] = visited[x][y] + 1
    
    cnt_move = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0 and visited[r][c] == -1:
                return -1
            elif visited[r][c] > -1 and cnt_move < visited[r][c]:
                cnt_move = visited[r][c]
    return cnt_move


cnt_empty = 0
for r in range(N):
    for c in range(N):
        if board[r][c] == 0:
            cnt_empty += 1

answers = []
for comb in combinations(virus_loc, n_virus):
    cnt = bfs(list(comb), cnt_empty)
    # FIXME - 그리고 수많은 조합 경우의 수 중에 도달할 수 없는 경우도 있고, 도달할 수 있는 경우도 있을 것
    answers.append(cnt)

valid_answers = [ans for ans in answers if ans != - 1]
if valid_answers:
    print(min(valid_answers))
else:
    print(-1)
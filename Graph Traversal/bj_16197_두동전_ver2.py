import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
board = [input() for _ in range(H)]

dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]


def in_board(x, y):
    if 0 <= x < H and 0 <= y < W:
        return True
    else:
        return False


def bfs(loc1, loc2):
    visited = [[False]*W for _ in range(H)]
    cnt_moved = 0
    
    q = deque([(loc_start, cnt_moved) ])
    visited[loc_start[0]][loc_start[1]] = True

    answer = -1
    while q:
        curr_loc, curr_cnt = q.popleft()
        
        for i in range(4):
            moved_x, moved_y = curr_loc[0]+dx[i], curr_loc[1]+dy[i]
            
            if not in_board(moved_x, moved_y):
                answer = curr_cnt+1
                break
            elif board[moved_x][moved_y] == '#':
                continue
            else:
                if visited[moved_x][moved_y]:
                    q.append(((moved_x, moved_y), curr_cnt+1 ) )
                    visited[moved_x][moved_y] = True
        
        if answer != -1 or answer > 10:
            break
    
    if answer > 10:
        answer = -1
        
    return answer


# Find the locations of coins.
coins_coord = []
for r in range(H):
    for c in range(W):
        if board[r][c] == 'o':
            coins_coord.append((r, c) )

coin1_loc, coin2_loc = coins_coord
coin_cnt = bfs(coin1_loc, coin2_loc)
print(coin_cnt)
import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
board = [input() for _ in range(H)]

dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]


def in_board(x, y):
    return 0 <= x < H and 0 <= y < W


def bfs(coin_pos1, coin_pos2):
    q = deque([ (coin_pos1, coin_pos2, 0) ])
    cnt = 0
    
    while q:
        coin1, coin2, cur_cnt = q.popleft()
        cur_x1, cur_y1 = coin1
        cur_x2, cur_y2 = coin2
        
        if cur_cnt == 10:
            return -1
        
        cnt = cur_cnt + 1
        for i in range(4):
            mx1, my1 = cur_x1+dx[i], cur_y1+dy[i]
            mx2, my2 = cur_x2+dx[i], cur_y2+dy[i]
            
            if in_board(mx1, my1) and in_board(mx2, my2):
                if board[mx1][my1] == '#':
                    nx1, ny1 = cur_x1, cur_y1
                else:
                    nx1, ny1 = mx1, my1
                    
                if board[mx2][my2] == '#':
                    nx2, ny2 = cur_x2, cur_y2
                else:
                    nx2, ny2 = mx2, my2
                    
                q.append(( (nx1, ny1), (nx2, ny2), cnt) )
        
            elif (in_board(mx1, my1) and not in_board(mx2, my2)) or \
            (not in_board(mx1, my1) and in_board(mx2, my2)):
                return cnt
        
        # FIXME - 이 부분 때문에 틀렸다. 아직 q에서 cnt == 9인 원소 다 탐색하지도 않았는데 cnt에 1 더해서 10 되면 종료시키기 때문이다.
        # if cnt == 10:
        #     return -1
    
    return cnt


coins_coord = []
for r in range(H):
    for c in range(W):
        if board[r][c] == 'o':
            coins_coord.append((r, c) )

coin1_loc, coin2_loc = coins_coord 
print(bfs(coin1_loc, coin2_loc))
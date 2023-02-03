import sys
from collections import deque

W, H = map(int, sys.stdin.readline().split())
board = []
depths = [[0]*W for _ in range(H)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
for _ in range(H):
    board.append(list(map(int, sys.stdin.readline().split())))

def bfs(q):
    curr_depth = 0
    while q:
        curr_loc = q.pop()
        curr_depth = depths[curr_loc[0]][curr_loc[1]]
        for x,y in zip(dx, dy):
            r = curr_loc[0] + x
            c = curr_loc[1] + y
            if 0 <= r and r < H and 0 <= c and c < W:
                if board[r][c] == 0:
                    q.appendleft((r, c))
                    board[r][c] = 1
                    depths[r][c] = curr_depth + 1
    for h in range(H):
        if 0 in board[h]:
            return -1
    return curr_depth


for h in range(H):
    for w in range(W):
        if board[h][w] == 1:
            q.appendleft((h, w))
print(bfs(q))


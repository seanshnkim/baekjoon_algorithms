import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_for_land(start_x, start_y, idx_island):
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    board[start_x][start_y] = idx_island
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            
            if 0 <= mx < N and 0 <= my < N and board[mx][my] == 1 and not visited[mx][my]:
                visited[mx][my] = True
                board[mx][my] = idx_island
                q.append((mx, my))


def bfs_for_path(cur_island):
    dist = [[-1]*N for _ in range(N)]
    q = deque()
    
    for r in range(N):
        for c in range(N):
            if board[r][c] == cur_island:
                q.append((r, c))
                dist[r][c] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]

            if not (0 <= mx < N and 0 <= my < N):
                continue
            
            if board[mx][my] > 0 and board[mx][my] != cur_island:
                return dist[x][y]
            
            if board[mx][my] == 0 and dist[mx][my] == -1:
                dist[mx][my] = dist[x][y] + 1
                q.append((mx, my))



# 1. 각 섬을 구분한다.
idx_island = 1
for r in range(N):
    for c in range(N):
        if not visited[r][c] and board[r][c] == 1:
            bfs_for_land(r, c, idx_island)
            idx_island += 1
            
# 각 섬 사이 최단 경로를 구한다.
answer = float('inf')
for cur_island in range(1, idx_island):
    cur_min = bfs_for_path(cur_island)
    answer = min(answer, cur_min)

print(answer)
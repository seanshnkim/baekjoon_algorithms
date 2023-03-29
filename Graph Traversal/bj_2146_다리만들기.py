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


def bfs_for_path(start_x, start_y, cur_island):
    q = deque([(start_x, start_y, 0)])
    tmp_visited = [[False]*N for _ in range(N)]
    tmp_visited[start_x][start_y] = True
    
    min_path = 2*N
    adj_island = 0
    
    while q:
        x, y, d = q.popleft()
        
        if board[x][y] > 0 and board[x][y] != cur_island:
            min_path = d-1
            adj_island = board[x][y]
            break
        
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]

            if 0 <= mx < N and 0 <= my < N and not tmp_visited[mx][my]:
                tmp_visited[mx][my] = True
                next_dist = 0
                
                if board[mx][my] == cur_island:
                    q.append((mx, my, 0))
                else:
                    q.append((mx, my, d+1))
    
    return min_path, adj_island



# 1. 각 섬을 구분한다.
idx_island = 1
for r in range(N):
    for c in range(N):
        if not visited[r][c] and board[r][c] == 1:
            bfs_for_land(r, c, idx_island)
            idx_island += 1
            

answer = float('inf')
visited_islands = set()
for cur_island in range(1, idx_island+1):
    for r in range(N):
        for c in range(N):
            if board[r][c] == cur_island:
                cur_min, adj_island = bfs_for_path(r, c, cur_island)
                visited_islands.add((cur_island, adj_island))
                
                answer = min(answer, cur_min)

print(answer)

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


def bfs_all_island(num_island):
    distances = [[-1]*N for _ in range(N)]
    queues = [deque() for _ in range(num_island)]
    visited = [[-1]*N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            for cur_island in range(1, num_island+1):
                if board[r][c] == cur_island:
                    queues[cur_island-1].append((0, r, c))
                    distances[r][c] = 0
                    visited[r][c] = cur_island
    
    # N*N 보드에서 섬 간 가능한 최대 거리는 2N-2, 근데 그냥 편의상 2*N이라 하자.
    for step in range(2*N):
        for cur_island in range(1, num_island+1):
            while queues[cur_island-1]:
                cur_d, x, y = queues[cur_island-1].popleft()
                
                if cur_d > step:
                    break
                
                for i in range(4):
                    mx, my = x+dx[i], y+dy[i]

                    if not (0 <= mx < N and 0 <= my < N):
                        continue
                    
                    if visited[mx][my] != -1 and visited[mx][my] != cur_island:
                        return cur_d + distances[mx][my]
                    
                    if board[mx][my] == 0 and distances[mx][my] == -1:
                        distances[mx][my] = cur_d + 1
                        queues[cur_island-1].append((cur_d+1, mx, my))
                        visited[mx][my] = cur_island
    
    # 디버깅을 위한 리턴값. 어떤 경우든 -1이 출력된다면 입력 테스트 케이스에 잘못이 있거나 코드에 문제가 있다는 뜻
    return -1
        


# 1. 각 섬을 구분한다.
idx_island = 1
for r in range(N):
    for c in range(N):
        if not visited[r][c] and board[r][c] == 1:
            bfs_for_land(r, c, idx_island)
            idx_island += 1

num_island = idx_island - 1
print(bfs_all_island(num_island))

'''
반례:
10
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1
'''
import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
# FIXME - 자료형 실수!!! 한참 헤맸다. 기록해두자.
# board = [[i for i in input()] for _ in range(H)]
board = [[int(i) for i in input().rstrip('\n')] for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0 , 0, 1, -1]

def bfs_with_wall(start_x, start_y, cnt_break):
    # visited[x][y] == -1: 아직 방문 X
    # visited[x][y] == 0: 벽을 부수지 않고 방문한 칸
    # visited[x][y] == 1: 벽을 한번 부수고(부수어야) 방문한 칸
    # visited[x][y] == 2: 벽을 2번 이상 부수어야 방문할 수 있는 칸, 더 이상 탐색하지 않음.
    visited = [[-1]*W for _ in range(H)]
    answer = -1
    # cnt_break = 0
    q = deque([(0, start_x, start_y)])
    visited[start_x][start_y] = 0
    
    while q:
        d, x, y = q.popleft()
        
        if x == H-1 and y == W-1:
            if answer == -1 or answer > d:
                answer = d
            break
        
        is_move_possible = False
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            
            if 0 <= mx < H and 0 <= my < W and visited[mx][my] == -1:
                if board[mx][my] == 0:
                    is_move_possible = True
                    q.append((d+1, mx, my))
                    visited[mx][my] = visited[x][y]
                    
        if not is_move_possible:
            if visited[x][y] >= 1:
                continue
            
            for i in range(4):
                mx, my = x+dx[i], y+dy[i]
                if 0 <= mx < H and 0 <= my < W and visited[mx][my] == -1:
                    q.append((d+1, mx, my))
                    visited[mx][my] = visited[x][y] + 1
    
    if answer == -1:
        return answer
    else:
        return answer + 1
            
'''
반례:
5 6                                   
000000
101111
001011
011010
000010
'''

print(bfs_with_wall(start_x=0, start_y=0, cnt_break=0))
import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
# FIXME - 자료형 실수!!! 한참 헤맸다. 기록해두자.
# board = [[i for i in input()] for _ in range(H)]
board = [[int(i) for i in input().rstrip('\n')] for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0 , 0, 1, -1]

def bfs_with_wall(start_x, start_y):
    visited = [[-1]*W for _ in range(H)]
    answer = -1
    # q의 원소 튜플: cur_dist, x좌표, y좌표
    q = deque([(0, 1, start_x, start_y)])
    visited[start_x][start_y] = 0
    
    while q:
        d, chance_break, x, y = q.popleft()
        
        if x == H-1 and y == W-1:
            if answer == -1 or answer > d:
                answer = d
            break
        
        if chance_break == 2:
            continue
        
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            
            # 이제는 visited[mx][my] == -1일 때만 탐색 X
            # 벽을 한번 뚫고 탐색한 경우(visited -> 0), 그 다음에 벽을 뚫지 않고 탐색한 경우 (visited -> 1)
            # 따라서, visited 값이 1 이상이면 방문 완료한 ?
            if 0 <= mx < H and 0 <= my < W:
                if board[mx][my] == 0:
                    if visited[mx][my] == 1:
                        continue
                    if visited[mx][my] == 3 and chance_break == 0:
                        continue
                    
                    if chance_break == 0:
                        visited[mx][my] = 3
                    else:
                        visited[mx][my] = 1
                        
                    q.append((d+1, chance_break, mx, my))
                    
                else:
                    if visited[mx][my] >= 1:
                        continue
                    if chance_break == 0:
                        continue
                        
                    q.append((d+1, chance_break-1, mx, my))

    
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

print(bfs_with_wall(start_x=0, start_y=0))
import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
board = [[i for i in input().rstrip('\n')] for _ in range(H)]
visited = [[False]*W for _ in range(H)]

dx = [-1, 1, 0,  0]
dy = [0,  0, -1, 1]

def find_deadends():
    deadends = []
    for x in range(H):
        for y in range(W):
            if board[x][y] == 'L':
                cnt = 0
                for i in range(4):
                    mx, my = x+dx[i], y+dy[i]
                    if 0 <= mx < H and 0 <= my < W and board[mx][my] == 'L':
                        cnt += 1
                if cnt == 1:
                    deadends.append((x, y))
    return deadends


def bfs(start_x, start_y):
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True
    
    max_dist = 0
    
    while q:
        x, y, d = q.popleft()
        
        if max_dist < d:
            max_dist = d
        
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            
            if 0 <= mx < H and 0 <= my < W and not visited[mx][my] and board[mx][my] == 'L':
                visited[mx][my] = True
                q.append((mx, my, d+1))
    
    return max_dist


def solution(deadends):
    global visited
    answer = 0
    if not deadends:
        for r in range(H):
            for c in range(W):
                if board[r][c] == 'L' and not visited[r][c]:
                    answer = max(answer, bfs(r, c))
    
    else:
        for r, c in deadends:
            answer = max(answer, bfs(r, c))
            visited = [[False]*W for _ in range(H)]
                
    return answer

print(solution(find_deadends()))
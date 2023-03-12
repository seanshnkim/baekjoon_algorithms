import sys
input = sys.stdin.readline
import heapq
from collections import deque

H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False]*W for _ in range(H)]
dp = [[-1]*W for _ in range(H)]
dp[0][0] = 1

next_steps = [(-board[0][0], (0, 0))]
# visited[0][0] = True
while next_steps:
    _, (x, y) = heapq.heappop(next_steps)
    
    if visited[x][y]:
        continue
    visited[x][y] = True
    
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if (0 <= mx < H and 0 <= my < W) and dp[mx][my] != -1 and board[x][y] < board[mx][my]:
            if dp[x][y] == -1:
                dp[x][y] = dp[mx][my]
            else:
                dp[x][y] += dp[mx][my]
            
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if (0 <= mx < H and 0 <= my < W) and board[mx][my] < board[x][y] and not visited[mx][my]:
            # min heap이 기본이기 때문에 - 부호를 붙여준다.
            heapq.heappush(next_steps, (-board[mx][my], (mx, my))  )


answer = dp[H-1][W-1]
if answer == -1:
    print(0)
else:
    print(answer)
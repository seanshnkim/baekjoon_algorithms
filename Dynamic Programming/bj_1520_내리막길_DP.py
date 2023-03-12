import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False]*W for _ in range(H)]
dp = [[-1]*W for _ in range(H)]
dp[0][0] = 1

q = deque([(0,0)])
while q:
    x, y = q.popleft()
    # q에는 같은 위치의 칸이 여러 개 중복해서 들어가 있을 수 있다. 이미 방문 처리한 것이라면 그냥 건너뛰도록 처리한다.
    if visited[x][y]:
        continue
    visited[x][y] = True
    
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if (0 <= mx < H and 0 <= my < W) and board[mx][my] < board[x][y] and not visited[mx][my]:
            if dp[mx][my] == -1:
                dp[mx][my] = dp[x][y]
            else:
                dp[mx][my] += dp[x][y]
            
            q.append((mx, my))

answer = dp[H-1][W-1]
if answer == -1:
    print(0)
else:
    print(answer)
    
'''
50 45 40 39
      30 37
      20
      19 18

50 45 40 
      30
      20
      19 18
      
50
45
40 39 20
      19 18
'''
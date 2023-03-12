import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False]*W for _ in range(H)]
dp = [[-1]*W for _ in range(H)]
dp[0][0] = 1

for x in range(H):
    for y in range(W):
        if dp[x][y] == -1:
            continue
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            if (0 <= mx < H and 0 <= my < W) and board[mx][my] < board[x][y]:
                if dp[mx][my] == -1:
                    dp[mx][my] = dp[x][y]
                else:
                    dp[mx][my] += dp[x][y]


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
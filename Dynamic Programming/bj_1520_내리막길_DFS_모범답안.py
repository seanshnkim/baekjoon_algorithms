import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dp = [[-1]*W for _ in range(H)]

def dfs(x, y):
    if x == H-1 and y == W-1:
        return 1
    
    if dp[x][y] >= 0:
        return dp[x][y]
    
    elif dp[x][y] == -1:
        dp[x][y] = 0
        
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            
            if (0 <= mx < H and 0 <= my < W) and board[mx][my] < board[x][y]:
                dp[x][y] += dfs(mx, my)
        
    return dp[x][y]


print(dfs(0, 0))
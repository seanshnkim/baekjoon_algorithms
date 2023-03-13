import sys
input = sys.stdin.readline
sys.setrecursionlimit(250000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def search(x, y):
    is_deadend = True
    cur_cnt = dp[x][y]
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if 0 <= mx < N and 0 <= my < N and board[x][y] < board[mx][my]:
            if dp[mx][my] == -1:
                search(mx, my)
            cur_cnt = max(cur_cnt, dp[mx][my])
            is_deadend = False
    
    if is_deadend:
        dp[x][y] = 1
    else:
        if dp[x][y] == -1 or dp[x][y] < cur_cnt:
            dp[x][y] = cur_cnt+1


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if dp[i][j] != -1:
            continue
        search(i, j)

print(max(max(row) for row in dp))
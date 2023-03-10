import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# cur_dir
# 0 -> 가로
# 1 -> 세로
# 2 -> 대각선
# x, y는 파이프의 오른쪽, 아래, 또는 대각선 오른쪽아래 끝의 위치를 의미
dp = [ [[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for x in range(N):
    for y in range(N):
        if x == 0 and y <= 1:
            continue
        if board[x][y] == 0:
            # 오른쪽
            if y > 0:
                dp[x][y][0] = dp[x][y-1][0] + dp[x][y-1][2]
                    
            # 아래
            if x > 0:
                dp[x][y][1] = dp[x-1][y][1] + dp[x-1][y][2]
            
            if x > 0 and y > 0:
                if board[x-1][y] == 0 and board[x][y-1] == 0:
                    dp[x][y][2] = sum(dp[x-1][y-1])

print(sum(dp[N-1][N-1]))
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [list(map(int, input().rstrip('\n') ) ) for _ in range(H)]
# dp[r][c] -> (r,c)를 오른쪽 아래 꼭짓점으로 하는 정사각형의 최대 크기
dp = [[0]*W for _ in range(H)]

for r in range(H):
    for c in range(W):
        if r == 0 or c == 0:
            # 맨 윗줄, 맨 왼쪽 줄은 크기가 1보다 큰 정사각형 생성할 수 없다ㅌ
            # 따라서 board[r][c] == 1이면 dp[r][c] = 1(크기가 1인 정사각형)
            dp[r][c] = board[r][c]
            continue
        if board[r][c] == 1:
            if dp[r][c-1] > 0 and dp[r][c-1] == dp[r-1][c]:
                width = dp[r][c-1]
                if board[r-width][c-width] == 1:
                    dp[r][c] = width+1
                else:
                    dp[r][c] = width
            else:
                smaller_width = min(dp[r][c-1], dp[r-1][c])
                dp[r][c] = smaller_width + 1

max_width = max(max(row) for row in dp)
answer = max_width * max_width
print(answer)

'''
11100000
11101111
11111111
01111111
01101111
00111000
11110000
00001100
'''
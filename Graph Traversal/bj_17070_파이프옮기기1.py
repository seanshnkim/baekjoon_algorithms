import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def in_board(x, y):
    return 0 <= x < N and 0 <= y < N

# cur_dir
# 0 -> 가로
# 1 -> 세로
# 2 -> 대각선
# x, y는 파이프의 오른쪽, 아래, 또는 대각선 오른쪽아래 끝의 위치를 의미
def move(cur_dir, x, y):
    if x == N-1 and y == N-1:
        return 1
    
    right = (0, x, y+1)
    down = (1, x+1, y)
    diag = (2, x+1, y+1)
    cnt = 0

    if cur_dir == 0:
        next_moves = [right, diag]
    elif cur_dir == 1:
        next_moves = [down, diag]
    else:
        next_moves = [right, down, diag]
        
    for dir, mx, my in next_moves:
        if in_board(mx, my) and board[mx][my] == 0:
            # 대각선이면 두 칸을 더 검사
            if dir == 2:
                if board[mx-1][my] == 0 and board[mx][my-1] == 0:
                    cnt += move(dir, mx, my)
            else:
                cnt += move(dir, mx, my)
    
    return cnt

print(move(0, 0, 1))
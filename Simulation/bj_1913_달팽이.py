import sys
input = sys.stdin.readline

# 홀수인 자연수이며, 1 ~ N^2까지 수를 N*N 크기의 배열에 나선형 모양으로 나열
N = int(input())
target = int(input())
board = [[0]*N for _ in range(N)]

# up, down, right, left
dx = [-1, 1, 0,  0]
dy = [0,  0, 1, -1]

# N >= 3
x, y = N//2, N//2
board[x][y] = 1
x -= 1
board[x][y] = 2
prev_dir = 0

ans_x, ans_y = 0, 0

# up(0)    -> right(2)를 확인
# down(1)  -> left(3) 를 확인
# right(2) -> down(1) 을 확인
# left(3)  -> up(0)   을 확인
for i in range(3, N*N+1):
    if prev_dir == 0:
        next_dir = 2
    elif prev_dir == 1:
        next_dir = 3
    elif prev_dir == 2:
        next_dir = 1
    else:
        next_dir = 0
    
    nx, ny = x+dx[next_dir], y+dy[next_dir]
    if board[nx][ny] == 0:
        prev_dir = next_dir

    x, y = x+dx[prev_dir], y+dy[prev_dir]
    board[x][y] = i
    
    if target == i:
        # 좌표는 1,1부터 시작한다.
        ans_x = x+1
        ans_y = y+1


for r in range(N):
    print(*board[r])

print(ans_x, ans_y)
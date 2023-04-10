import sys
input = sys.stdin.readline

H, W = map(int, input().split())
visited = [[False]*W for _ in range(H)]
# up, down, left, right
dx = [-1, 1,  0, 0]
dy = [0,  0, -1, 1]

x, y = 0, 0
visited[x][y] = True

y += 1
visited[x][y] = True
prev_dir = 3
cnt_move = 1
cnt_turn = 0

while cnt_move < H*W-1:
    if prev_dir == 0:
        next_dir = 3
    elif prev_dir == 1:
        next_dir = 2
    elif prev_dir == 2:
        next_dir = 0
    else:
        next_dir = 1
        
    # 일단 기존 방향대로 전진
    nx, ny = x+dx[prev_dir], y+dy[prev_dir]
    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny]:
        x, y = nx, ny
        visited[x][y] = True
    else:
        x, y = x+dx[next_dir], y+dy[next_dir]
        visited[x][y] = True
        prev_dir = next_dir
        cnt_turn += 1
    
    cnt_move += 1


print(cnt_turn)
# 문제에선 (1, 1)부터 시작한다.
print(x+1, y+1)
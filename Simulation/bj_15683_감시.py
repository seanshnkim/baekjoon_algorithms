import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

# 일단 각 cctv마다 감시 가능 칸 수 구하는(벽 고려해서)
# -> 칸 개수만 구하는 게 아니라 board에 직접 기록해야 한다. visited 배열 쓰든지
# 그리고 순회해야 한다.
# 모든 CCTV 개수에 대해 완전탐색하면 된다. -> 최소를 구하면 된다.



def fill(dir, x, y, visited):
    # East
    if dir == 0:
        for c in range(y+1, W):
            if board[x][c] == 6:
                break
            if not visited[x][c]:
                visited[x][c] = True
    # West
    elif dir == 1:
        for c in range(y-1, -1, -1):
            if board[x][c] == 6:
                break
            if not visited[x][c]:
                visited[x][c] = True
    
    # South
    elif dir == 2:
        for r in range(x+1, H):
            if board[r][y] == 6:
                break
            if not visited[r][y]:
                visited[r][y] = True
    # North
    else:
        for r in range(x-1, -1, -1):
            if board[r][y] == 6:
                break
            if not visited[r][y]:
                visited[r][y] = True
    

    



# iter_cnt = 0, 1, 2, 3
def simulate(dir, x, y, visited):
    if board[x][y] == 1:
        fill(dir, x, y, visited)
    
    elif board[x][y] == 2:
        fill(dir, x, y, visited)
        if dir <= 1:
            fill((dir+1)%2, x, y, visited)
        else:
            fill((dir+1)%2+2, x, y, visited)

    elif board[x][y] == 3:
        fill(dir, x, y, visited)
        
        if dir == 0:
            fill(3, x, y, visited)
        elif dir == 1:
            fill(2, x, y, visited)
        elif dir == 2:
            fill(0, x, y, visited)
        else:
            fill(1, x, y, visited)
            
        
    elif board[x][y] == 4:
        fill(dir, x, y, visited)
        
        if dir == 0:
            fill(3, x, y, visited)
            fill(1, x, y, visited)
        elif dir == 1:
            fill(2, x, y, visited)
            fill(0, x, y, visited)
        elif dir == 2:
            fill(0, x, y, visited)
            fill(3, x, y, visited)
        else:
            fill(1, x, y, visited)
            fill(2, x, y, visited)
        
    else:
        for d in range(4):
            fill(d, x, y, visited)
    

num_cctv = 0
visited_init = [[False]*W for _ in range(H)]
for r in range(H):
    for c in range(W):
        if board[r][c] != 0:
            visited_init[r][c] = True
        if 1 <= board[r][c] <= 5:
            num_cctv += 1
        
answer = H*W
for i in range(1 << num_cctv*2):
    visited = [row.copy() for row in visited_init]
    cnt = 0
    for r in range(H):
        for c in range(W):
            if 1 <= board[r][c] <= 5:
                k = (i >> (cnt*2)) & 3
                simulate(k, r, c, visited)
                cnt += 1
                
    min_cnt = sum(sum(1 if not visited[r][c] else 0 for c in range(W)) \
                  for r in range(H))
    answer = min(answer, min_cnt)

print(answer)
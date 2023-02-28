import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N) ]
built = [[False]*N for _ in range(N)]

answer = 0

# 행 탐색 
for r in range(N):
    path_exists = True
    for c in range(N-1):
        curr_val = board[r][c]
        
        if curr_val > board[r][c+1]:
            if not (curr_val - board[r][c+1] == 1):
                path_exists = False
                break
            else:
                for i in range(c+1, c+L+1):
                    # board의 N*N 범위를 벗어나거나 높이가 일정하지 않거나, 
                    if i >= N or board[r][i] != board[r][c+1] or built[r][i]:
                        path_exists = False
                        break
                if path_exists:
                    for i in range(c+1, c+L+1):
                        built[r][i] = True
        elif curr_val < board[r][c+1]:
            if not (board[r][c+1] - curr_val == 1):
                path_exists = False
                break
            else:
                # for i in range(c-1, c-L, -1):
                for i in range(c, c-L, -1):
                    if i < 0 or board[r][i] != curr_val or built[r][i]:
                        path_exists = False
                        break
                if path_exists:
                    for i in range(c-1, c-L, -1):
                        built[r][i] = True
        if not path_exists:
            break
        
    if path_exists:
        answer += 1


built = [[False]*N for _ in range(N)]
# 열 탐색
for c in range(N):
    path_exists = True
    for r in range(N-1):
        curr_val = board[r][c]
        
        if curr_val > board[r+1][c]:
            if not (curr_val - board[r+1][c] == 1):
                path_exists = False
                break
            else:
                for i in range(r+1, r+L+1):
                    # board의 N*N 범위를 벗어나거나 
                    if i >= N or board[i][c] != board[r+1][c] or built[i][c]:
                        path_exists = False
                        break
                if path_exists:
                    for i in range(r+1, r+L+1):
                        built[i][c] = True
                        
        elif curr_val < board[r+1][c]:
            if not (board[r+1][c] - curr_val == 1):
                path_exists = False
                break
            else:
                for i in range(r-1, r-L, -1):
                    if i < 0 or board[i][c] != curr_val or built[i][c]:
                        path_exists = False
                        break
                if path_exists:
                    for i in range(r-1, r-L, -1):
                        built[i][c] = True
        if not path_exists:
            break
        
    if path_exists:
        answer += 1

print(answer)
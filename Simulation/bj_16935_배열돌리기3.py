import sys


def compute(opt, board):
    H = len(board)
    W = len(board[0])
    output_board = [[0]*W for _ in range(H)]
    
    if opt == 1 or opt == 2:
        for r in range(H):
            for c in range(W):
                sub = board[H-1-r][c]
                if opt == 2:
                    sub = board[r][W-1-c]
                output_board[r][c] = sub

    elif opt == 3 or opt == 4:
        output_board = [[0]*H for _ in range(W)]
        for r in range(W):
            for c in range(H):
                sub = board[H-1-c][r]
                if opt == 4:
                    sub = board[c][W-1-r]
                output_board[r][c] = sub
    else:
        for r in range(H//2):
            for c in range(W//2):
                if opt == 5:
                    # 4번 그룹을 1번 그룹으로 이동
                    output_board[r][c] = board[r+H//2][c]
                else:
                    # 1번 그룹을 4번 그룹으로 이동
                    output_board[r+H//2][c] = board[r][c]
                    
        for r in range(H//2, H):
            for c in range(W//2):
                # 3번 그룹을 4번 그룹으로 이동
                if opt == 5:
                    output_board[r][c] = board[r][c+W//2]
                # 4번 그룹을 3번 그룹으로 이동
                else:
                    output_board[r][c+W//2] = board[r][c]
        
        for r in range(H//2, H):
            for c in range(W//2, W):
                # 2번 그룹을 3번 그룹으로 이동
                if opt == 5:
                    output_board[r][c] = board[r-H//2][c]
                # 3번 그룹을 2번 그룹으로 이동
                else:
                    output_board[r-H//2][c] = board[r][c]
        
        # 1번 그룹을 2번 그룹으로 이동
        for r in range(H//2):
            for c in range(W//2, W):
                if opt == 5:
                    output_board[r][c] = board[r][c-W//2]
                else:
                    output_board[r][c-W//2] = board[r][c]
        
        
    return output_board


height, width, n_compute = map(int, sys.stdin.readline().split())
board = []
for _ in range(height):
    board.append(list(map(int, sys.stdin.readline().split())))

options = list(map(int, sys.stdin.readline().split()))
for opt in options:
    board = compute(opt, board)

new_height = len(board)
for h in range(new_height):
    print(*board[h])
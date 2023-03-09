dx = [0,0,1,-1]
dy = [1,-1,0,0]
LIMIT = 5

def generate_dir(k):
    a = [0]*LIMIT
    for i in range(LIMIT):
        a[i] = (k&3)
        k >>= 2
    return a


def check(board, dirs):
    length = len(board)
    board_copy = [row[:] for row in board]

    for dir in dirs:
        ok = False
        merged = [[False]*length for _ in range(length)]
        
        while True:
            ok = False
            if dir == 0:
                for r in range(length-2, -1, -1):
                    for c in range(length):
                        if board_copy[r][c] == 0:
                            continue
                        if board_copy[r+1][c] == 0:
                            board_copy[r+1][c] = board_copy[r][c]
                            merged[r+1][c] = merged[r][c]
                            board_copy[r][c] = 0
                            ok = True
                        elif board_copy[r+1][c] == board_copy[r][c]:
                            if not merged[r][c] and not merged[r+1][c]:
                                board_copy[r+1][c] *= 2
                                merged[r+1][c] = True
                                board_copy[r][c] = 0
                                ok = True
            elif dir == 1:
                for r in range(1, length):
                    for c in range(length):
                        if board_copy[r][c] == 0:
                            continue
                        if board_copy[r-1][c] == 0:
                            board_copy[r-1][c] = board_copy[r][c]
                            merged[r-1][c] = merged[r][c]
                            board_copy[r][c] = 0
                            ok = True
                        elif board_copy[r-1][c] == board_copy[r][c]:
                            if not merged[r][c] and not merged[r-1][c]:
                                board_copy[r-1][c] *= 2
                                merged[r-1][c] = True
                                board_copy[r][c] = 0
                                ok = True
            elif dir == 2:
                for c in range(1, length):
                    for r in range(length):
                        if board_copy[r][c] == 0:
                            continue
                        if board_copy[r][c-1] == 0:
                            board_copy[r][c-1] = board_copy[r][c]
                            merged[r][c-1] = merged[r][c]
                            board_copy[r][c] = 0
                            ok = True
                        elif board_copy[r][c-1] == board_copy[r][c]:
                            if not merged[r][c] and not merged[r][c-1]:
                                board_copy[r][c-1] *= 2
                                merged[r][c-1] = True
                                board_copy[r][c] = 0
                                ok = True
            elif dir == 3:
                for c in range(length-2, -1, -1):
                    for r in range(length):
                        if board_copy[r][c] == 0:
                            continue
                        if board_copy[r][c+1] == 0:
                            board_copy[r][c+1] = board_copy[r][c]
                            merged[r][c+1] = merged[r][c]
                            board_copy[r][c] = 0
                            ok = True
                        elif board_copy[r][c+1] == board_copy[r][c]:
                            if not merged[r][c] and not merged[r][c+1]:
                                board_copy[r][c+1] *= 2
                                merged[r][c+1] = True
                                board_copy[r][c] = 0
                                ok = True
            if not ok:
                break

    ans = max([max(row) for row in board_copy])
    return ans


N = int(input())
board_init = [list(map(int,input().split())) for _ in range(N)]
answer = 0

for k in range(1<<(LIMIT*2)):
    dirs = generate_dir(k)
    answer = max(answer, check(board_init, dirs))
    
print(answer)
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
start_x, start_y, ori = map(int, input().split())
board = [list(map(int, input().split()) ) for _ in range(H) ]

# if start_coord == (-1,-1):
#     print(0)
#     sys.exit(0)

# 0    , 1   , 2,     3
# north, east, south, west
dx = [-1, 0, 1,  0]
dy = [ 0, 1, 0, -1]


def in_board(x, y):
    return 0 <= x < H and 0 <= y < W


def rotate_90(orient):
    if orient == 3:
        return 0
    else:
        return orient+1
    
    
# 0    , 1   , 2,     3
# north, east, south, west
def back(x, y, orient):
    if orient == 0:
        return (x+1, y)
    elif orient == 1:
        return (x, y-1)
    elif orient == 2:
        return (x-1, y)
    else:
        return (x, y+1)

answer = 0
curr_x, curr_y = start_x, start_y
# while문 고쳐야 함
while True:
    if board[curr_x][curr_y] == 0:
        board[curr_x][curr_y] = -1
        answer += 1
        
    cnt_uncleaned = 0
    
    for i in range(4):
        moved_x, moved_y = curr_x+dx[i], curr_y+dy[i]
        if in_board(moved_x, moved_y) and board[moved_x][moved_y] == 0:
            cnt_uncleaned += 1
    if cnt_uncleaned > 0:
        ori = rotate_90(ori)
        moved_x, moved_y = curr_x+dx[ori], curr_y+dy[ori]
        if in_board(moved_x, moved_y) and board[moved_x][moved_y] == 0:
            curr_x, curr_y = moved_x, moved_y
    else:
        backed_x, backed_y = back(curr_x, curr_y, ori)
        if (not in_board(backed_x, backed_y)) or board[backed_x][backed_y] == 1:
            break
        else:
            curr_x, curr_y = backed_x, backed_y

print(answer)
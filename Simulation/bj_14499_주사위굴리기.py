import sys
input = sys.stdin.readline

H, W, x, y, n_comm = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
dice = [0]*7
# 위, 아래, 왼쪽(서쪽), 오른쪽(동쪽)
dx = [0, 0,  0, -1, 1]
dy = [0, 1, -1,  0, 0]

def move(command):
    # 동쪽 East
    dice_before = dice.copy()
    #FIXME - local variable 'x' referenced before assignment
    # moved_x, moved_y = x+dx[command], y+dy[command]
    global x, y
    moved_x, moved_y = x+dx[command], y+dy[command]
    
    if 0 <= moved_x < H and 0 <= moved_y < W:
        if command == 1:
            dice[1] = dice_before[4]
            dice[3] = dice_before[1]
            dice[4] = dice_before[6]
            dice[6] = dice_before[3]
        # 서쪽 West
        elif command == 2:
            dice[1] = dice_before[3]
            dice[3] = dice_before[6]
            dice[4] = dice_before[1]
            dice[6] = dice_before[4]
        # 북쪽 North
        elif command == 3:
            dice[1] = dice_before[5]
            dice[2] = dice_before[1]
            dice[5] = dice_before[6]
            dice[6] = dice_before[2]
        # 남쪽 South
        elif command == 4:
            dice[1] = dice_before[2]
            dice[2] = dice_before[6]
            dice[5] = dice_before[1]
            dice[6] = dice_before[5]
        
        if board[moved_x][moved_y] == 0:
            board[moved_x][moved_y] = dice[6]
        else:
            dice[6] = board[moved_x][moved_y]
            board[moved_x][moved_y] = 0
        
        # move x,y
        x, y = moved_x, moved_y
        
        print(dice[1])
    


commands = list(map(int, input().split()))
for com in commands:
    move(com)

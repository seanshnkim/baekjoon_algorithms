import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
answer = 0

def move(direction, board):
    if direction == 0:
        # 위
        for c in range(n):
            arr = []
            for r in range(n):
                if board[r][c]!= 0:
                    arr.append(board[r][c])
            moved_arr = []
            if len(arr) == 1:
                moved_arr.append(arr[0])
            else:
                for i in range(1,len(arr)):
                    if arr[i-1] == arr[i]:
                        moved_arr.append(arr[i] * 2)
                        arr[i] = 0
                    else:
                        if arr[i-1] != 0:
                            moved_arr.append(arr[i-1])
                        if i == len(arr)-1:
                            moved_arr.append(arr[i])
                # print(moved_arr)
            for i in range(len(moved_arr)):
                board[i][c] = moved_arr[i]
            for i in range(len(moved_arr),n):
                board[i][c] = 0
            # print(board)
    elif direction == 1:
        # 왼
        for r in range(n):
            arr = []
            for c in range(n):
                if board[r][c] != 0:
                    arr.append(board[r][c])
            moved_arr = []
            if len(arr) == 1:
                moved_arr.append(arr[0])
            else:
                for i in range(1,len(arr)):
                    if arr[i-1] == arr[i]:
                        moved_arr.append(arr[i] * 2)
                        arr[i] = 0
                    else:
                        if arr[i-1] != 0:
                            moved_arr.append(arr[i-1])
                        if i == len(arr)-1:
                            moved_arr.append(arr[i])
                # print(moved_arr)
            for i in range(len(moved_arr)):
                board[r][i] = moved_arr[i]
            for i in range(len(moved_arr),n):
                board[r][i] = 0
            # print(board)
        # pass
    elif direction == 2:
        # 아래
        for c in range(n):
            arr = []
            for r in range(n-1,-1,-1):
                if board[r][c]!= 0:
                    arr.append(board[r][c])
            moved_arr = []
            if len(arr) == 1:
                moved_arr.append(arr[0])
            else:
                for i in range(1,len(arr)):
                    if arr[i-1] == arr[i]:
                        moved_arr.append(arr[i] * 2)
                        arr[i] = 0
                    else:
                        if arr[i-1] != 0:
                            moved_arr.append(arr[i-1])
                        if i == len(arr)-1:
                            moved_arr.append(arr[i])
            for i in range(len(moved_arr)):
                board[n-1-i][c] = moved_arr[i]
            for i in range(n-len(moved_arr)-1,-1,-1):
                board[i][c] = 0
    elif direction == 3:
        for r in range(n):
            arr = []
            for c in range(n-1,-1,-1):
                if board[r][c] != 0:
                    arr.append(board[r][c])
            moved_arr = []
            if len(arr) == 1:
                moved_arr.append(arr[0])
            else:
                for i in range(1,len(arr)):
                    if arr[i-1] == arr[i]:
                        moved_arr.append(arr[i] * 2)
                        arr[i] = 0
                    else:
                        if arr[i-1] != 0:
                            moved_arr.append(arr[i-1])
                        if i == len(arr)-1:
                            moved_arr.append(arr[i])
                            
            for i in range(len(moved_arr)):
                board[r][n-1-i] = moved_arr[i]
            for i in range(n-len(moved_arr)-1,-1,-1):
                board[r][i] = 0


order = []

def dfs(l):
    global answer
    if l == 5:
        initial_board = [board[i][::] for i in range(n)]
        for direction in order:
            # direction별 이동
            move(direction, initial_board)
        # print(initial_board)
        max_value = max([max(initial_board[i]) for i in range(n)])
        # print(max_value)
        answer = max(answer, max_value)
        return
    
    # 0 -> 위, 1 -> 왼, 2 -> 아래, 3 -> 오
    for i in range(4):
        order.append(i)
        dfs(l+1)
        order.pop()


dfs(0)
print(answer)
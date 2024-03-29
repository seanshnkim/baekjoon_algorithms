import sys
input = sys.stdin.readline

def calc1():
    board2 = [[0] * m for _ in range(n)]
    for i in range(n):
        board2[i] = board[n-i-1]
    return board2

def calc2():
    board2 = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            board2[i][j] = board[i][m-j-1]
    return board2

def calc3(board,n,m):
    board2 = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            board2[i][j] = board[n-j-1][i]
    return board2

def calc4(board,n,m):
    board2 = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            board2[i][j] = board[j][m-i-1]
    return board2

def calc5():
    board2 = [[0] * m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            board2[i][j+m//2] = board[i][j]
    
    for i in range(n//2):
        for j in range(m//2,m):
            board2[i+n//2][j] = board[i][j]
    
    for i in range(n//2,n):
        for j in range(m//2):
            board2[i-n//2][j] = board[i][j]
    
    for i in range(n//2,n):
        for j in range(m//2,m):
            board2[i][j-m//2] = board[i][j]

    return board2
def calc6():
    board2 = [[0] * m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            board2[i+n//2][j] = board[i][j]
        
    for i in range(n//2,n):
        for j in range(m//2):
            board2[i][j+m//2] = board[i][j]
    
    for i in range(n//2):
        for j in range(m//2,m):
            board2[i][j-m//2] = board[i][j]
    
    for i in range(n//2,n):
        for j in range(m//2,m):
            board2[i-n//2][j] = board[i][j]

    return board2
n,m,R = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
orders = list(map(int,input().split()))

for order in orders:
    if order == 1:
        board = calc1()

    elif order == 2:
        board = calc2()

    elif order == 3:
        board = calc3(board,n,m)
        n,m = m,n

    elif order == 4:
        board = calc4(board,n,m)
        n,m = m,n

    elif order == 5:
        board = calc5()
    else:
        board = calc6()
    
for i in board:
    print(*i)
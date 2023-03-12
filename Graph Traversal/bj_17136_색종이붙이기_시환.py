import sys
from collections import deque
board = [list(map(int,input().split())) for _ in range(10)]
count = 0
counts = [0,5,5,5,5,5]
answer = 25
start = -1
for r in range(10):
    for c in range(10):
        if board[r][c] == 1 and start == -1:
                start = (r,c)

def check_possible_area(board, r, c, m):
    for row in range(r,r+m):
        for col in range(c,c+m):
            if board[row][col] == 0:
                return False
    return True


def fill(board, r, c, m, num):
    for row in range(r, r+m):
        for col in range(c, c+m):
            board[row][col] = num

def find_max(board,row,col):
    for i in range(5,0,-1):
        if row+i-1 >= 10 or col+i-1 >=10:
            continue
        if check_possible_area(board, row, col, i):
            return i
    return 0
        

def find_next(r,c):
    num = 10 * r + c
    
    while True:
        num += 1
        if num == 100:
            return False
        if board[num//10][num%10] == 1:
            return (num//10, num%10)
        


def backtracking(r,c,paper_count):
    global count
    global answer
    global board
    global counts
    max_length = find_max(board,r,c)
    for i in range(max_length, 0, -1):
        if counts[i] == 0:
            continue

        fill(board, r, c, i, 0)
        counts[i] -= 1
        if find_next(r,c) == False:
            answer = min(answer, paper_count+1)
        else:
            next_r,next_c = find_next(r,c)
            backtracking(next_r, next_c, paper_count+1)

        fill(board,r,c,i,1)
        counts[i] += 1


if start == -1:
    print(0)
else:
    start_row,start_col = start
    backtracking(start_row, start_col,0)
    if answer == 25:
        print(-1)
    else:
        print(answer)
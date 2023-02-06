import sys
input = sys.stdin.readline

height, width, n_rotate = map(int, input().split())
input_board = [list(map(int, input().split())) for _ in range(height)]

def rotate_counter_clockwise(num_rotate, board):
    new_board = [[0]*width for _ in range(height)]
    
    for n in range(num_rotate):
        row_start, row_end = 0, height
        col_start, col_end = 0, width
        
        r, c = row_start+1, col_start
        while row_start < row_end and col_start < col_end:
            while r < row_end:
                new_board[r][c] = board[r-1][c]
                r += 1
            r -= 1
            while c < col_end-1:
                new_board[r][c+1] = board[r][c]
                c += 1
            while r > row_start:
                new_board[r-1][c] = board[r][c]
                r -= 1
            while c > col_start:
                new_board[r][c-1] = board[r][c]
                c -= 1
                
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
            r, c = row_start+1, col_start
        
        #FIXME - 에러의 원인: new_board 리스트에서 값의 업데이트가 그대로 board에도 적용된다.
        board = new_board.copy()

    return new_board


result_board = rotate_counter_clockwise(n_rotate, input_board)
for row in result_board:
    print(*row)
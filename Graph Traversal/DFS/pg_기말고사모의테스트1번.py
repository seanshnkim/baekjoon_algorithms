import sys
sys.setrecursionlimit(400)

def solution(rows, columns, max_virus, queries):
    
    board = [[0]*columns for _ in range(rows)]
    # up, down, left, right
    dx = [-1, 1, 0,  0]
    dy = [ 0, 0, -1, 1]

    visited = [[False]*columns for _ in range(rows)]

    def in_board(x, y):
        return 0 <= x < rows and 0 <= y < columns

    def proliferate(x,y):
        if board[x][y] < max_virus:
            board[x][y] += 1
            return

        for i in range(4):
            mx, my = x+dx[i], y+dy[i]

            if in_board(mx, my):
                visited[mx][my] = True
                proliferate(mx, my)
                visited[mx][my] = False
        return
            

    for query in queries:
        x, y = query
        # 주어지는 입력 query는 행,열을 1부터 시작하고
        # 내 풀이는 리스트 0번째 인덱스부터 시작하므로 1씩 빼주어야
        visited[x-1][y-1] = True
        proliferate(x-1,y-1)
        visited[x-1][y-1] = False
    
    return board

test_q = [[3,2]]
print(solution(3,4,2, test_q))
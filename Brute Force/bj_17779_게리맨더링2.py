import sys
input = sys.stdin.readline

N = int(input())
demography = [list(map(int, input().split())) for _ in range(N)]

# 선거구를 나누었다고 가정할 때, 인구 최대 선거구 vs. 최소 선거구의 인구 차이를 구하는 함수
def diff(board):
    population = [0]*5
    
    for r in range(N):
        for c in range(N):
            # 만약 board[r][c] == k이면 k번째 원소에 해당 선거구 인구만큼 population 원소에 더해
            idx_reg = board[r][c] # idx_reg: 0 ~ 4
            cur_pop = demography[r][c]
            population[idx_reg] += cur_pop
    
    return max(population) - min(population)


# 기준점 (x, y)와 경계의 길이 (d1, d2)가 주어졌을 때 선거구를 나누는 방식
def partition(x, y, d1, d2):
    # 5번 선거구를 '4'로 표시. 0번 선거구 = '1'
    board = [[4]*N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if 0 <= r < x+d1-1 and 0 <= c <= y-1:
                board[r][c] = 0
            elif 0 <= r <= x+d2-1 and y-1 < c <= N-1:
                board[r][c] = 1
            elif x+d1-1 <= r <= N-1 and 0 <= c < y-d1+d2-1:
                board[r][c] = 2
            elif x+d2-1 < r <= N-1 and y-d1+d2-1 <= c <= N-1:
                board[r][c] = 3

    for i in range(d1+1):
        board[x-1 + i][y-1 - i] = 4
        board[x-1+d2 + i][y-1+d2 - i] = 4
    for i in range(d2+1):
        board[x-1 + i][y-1 + i] = 4
        board[x-1+d1 + i][y-1-d1 + i] = 4
    
    for r in range(N):
        for c in range(N):
            if board[r][c] == 4:
                left_end = c
                right_end = c
                for k in range(N-1, c, -1):
                    if board[r][k] == 4:
                        right_end = k
                for cc in range(left_end, right_end+1):
                    board[r][cc] = 4 
    
    return board


for x in range()


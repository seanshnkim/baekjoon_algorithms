import sys
input = sys.stdin.readline
BSIZE = 10
board = [list(map(int, input().split())) for _ in range(BSIZE)]
# visited[x][y] == 1이면 채워야 하는 칸, == 0이면 채우면 안되는 칸
# visited[x][y] == 1이었고 방문했다면 해당 정사각형(색종이)의 크기로 변경하기로 하자.
visited = [row.copy() for row in board]

# cnt_left[k] = k*k 크기의 색종이 남은 개수
cnt_left = [0, 5, 5, 5, 5, 5]


def find_largest_square(x, y):
    max_width = 1
    # max_width가 5가 넘으면 안된다.
    while x+max_width <= BSIZE and y+max_width <= BSIZE and max_width <= 5:
        for r in range(max_width):
            for c in range(max_width):
                if visited[x+r][y+c] != 1:
                    max_width -= 1
                    return max_width
        max_width += 1
    
    max_width -= 1
    return max_width


def cover(x, y, width, fill_val):
    for r in range(width):
        for c in range(width):
            visited[x+r][y+c] = fill_val+1


def find_next():
    for r in range(BSIZE):
        for c in range(BSIZE):
            if visited[r][c] == 1:
                return (r, c)
    return (-1, -1)


def solution(start_x, start_y, cnt):
    max_width = find_largest_square(start_x, start_y)
    cur_cnt = -1
    
    for width in range(max_width, 0, -1):
        if cnt_left[width] == 0:
            continue
        
        cnt_left[width] -= 1
        cover(start_x, start_y, width=width, fill_val=width)
        next_pos = find_next()
        
        if next_pos == (-1, -1):
            # 재귀함수니까 다시 visited 해제
            cnt_left[width] += 1
            cover(start_x, start_y, width=width, fill_val=0)
            
            if cur_cnt == -1:
                cur_cnt = cnt+1
            else:
                cur_cnt = min(cur_cnt, cnt+1)
        else:
            # 항상 채워야 할(아직 1인) 칸만 solution 함수에 입력해야 함
            res = solution(next_pos[0], next_pos[1], cnt+1)
            cnt_left[width] += 1
            cover(start_x, start_y, width=width, fill_val=0)
            
            if res == -1:
                continue
        
            if cur_cnt == -1 or cur_cnt > res:
                cur_cnt = res
            # FIXME - 이게 87% 구간에서 틀린 원인이었다. Line 75 ~ 76
            # elif cur_cnt <= res:
            #     break

    return cur_cnt


def find_start(board):
    for r in range(BSIZE):
        for c in range(BSIZE):
            if board[r][c] == 1:
                return (r, c)
    return (-1, -1)


start_x, start_y = find_start(board)
answer = 0
if (start_x, start_y) != (-1, -1):
    answer = solution(start_x, start_y, 0)
print(answer)
import sys
input = sys.stdin.readline
BSIZE = 10
board = [list(map(int, input().split())) for _ in range(BSIZE)]
# visited[x][y] == 1이면 채워야 하는 칸, == 0이면 채우면 안되는 칸
# visited[x][y] == 1이었고 방문했다면 2로 변경하기로 하자.
visited = [row.copy() for row in board]

# cnt_left[k] = k*k 크기의 색종이 남은 개수
cnt_left = [0, 5, 5, 5, 5, 5]


# 최대 10*10 크기의 보드이므로 시간복잡도는 그리 크지 않을 것이다.
def is_all_covered(visited):
    for r in range(BSIZE):
        for c in range(BSIZE):
            # 즉, 아직 방문하지 않은 (그러나 채워야했던) 칸이 있다면
            if visited[r][c] == 1:
                return False
    return True


# (x, y)를 기준으로, 오른쪽과 아래를 탐색해나가면서 색종이로 덮을 수 있는
# (즉, 각 칸에 담긴 숫자가 모두 1인) 최대 정사각형의 길이를 구한다.
def find_largest_square(x, y):
    max_width = 1
    
    while x+max_width < BSIZE and y+max_width < BSIZE:
        for r in range(max_width):
            for c in range(max_width):
                if board[x+r][y+c] != 1:
                    return max_width-1
        max_width += 1
    
    return max_width-1


# cover 함수는, 해당 덮고자(cover) 하는 영역이 모두 보드 경계 안에 있고
# 모두 채워야 하는 칸(1인 칸)임이 확인되고 나서 수행한다.
def cover(x, y, max_width):
    for r in range(max_width):
        for c in range(max_width):
            visited[x+r][y+c] = 2

def uncover(x, y, max_width):
    for r in range(max_width):
        for c in range(max_width):
            visited[x+r][y+c] = 1
            

def next_fill(visited):
    for r in range(BSIZE):
        for c in range(BSIZE):
            if visited[r][c] == 1:
                return (r, c)
    return (-1, -1)


def solution(start_x, start_y, cnt):
    max_width = find_largest_square(start_x, start_y)
    width = max_width
    # visited[r][c] == 1이기 때문에 max_width 리턴값은 항상 1 이상
    # if max_width > 0:
    cur_cnt = -1
    while width >= 1:
        if cnt_left[width] == 0:
            width -= 1
        else:
            cnt_left[width] -= 1
            cover(start_x, start_y, width)
            next_pos = next_fill(visited)
            
            if next_pos != (-1, -1):
                # 항상 채워야 할(아직 1인) 칸만 solution 함수에 입력해야 함
                res = solution(next_pos[0], next_pos[1], cnt+1)
                # 현재 width는 유효하지 않다는 뜻
                if res == -1:
                    cnt_left[width] += 1
                    uncover(start_x, start_y, width)
                    break
                else:
                    # 현재까지의 cnt : cnt, 앞으로의 cnt : res
                    if cur_cnt == -1 or cur_cnt > cnt + res:
                        cur_cnt = cnt + res
                        # 재귀함수니까 다시 visited 해제해주어야 함
                    cnt_left[width] += 1
                    uncover(start_x, start_y, width)
                    width -= 1
            # 다 채웠다면. 반드시 width = max_width일 때 발생
            else:
                cnt_left[width] += 1
                uncover(r, c, width)
                return cnt+1

    return cur_cnt


start_x = -1
start_y = -1
for r in range(BSIZE):
    for c in range(BSIZE):
        if board[r][c] == 1:
            start_x, start_y = r, c
            break
        
print(solution(start_x, start_y, 0))
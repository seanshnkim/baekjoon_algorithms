import sys
input = sys.stdin.readline
BSIZE = 10
board = [list(map(int, input().split())) for _ in range(BSIZE)]
# visited[x][y] == 1이면 채워야 하는 칸, == 0이면 채우면 안되는 칸
# visited[x][y] == 1이었고 방문했다면 2로 변경하기로 하자.
visited = [row.copy() for row in board]

# cnt_left[k] = k*k 크기의 색종이 남은 개수
cnt_left = [0, 5, 5, 5, 5, 5]


# (x, y)를 기준으로, 오른쪽과 아래를 탐색해나가면서 색종이로 덮을 수 있는
# (즉, 각 칸에 담긴 숫자가 모두 1인) 최대 정사각형의 길이를 구한다.
def find_largest_square(x, y):
    max_width = 1
    # max_width가 5가 넘으면 안된다.
    while x+max_width <= BSIZE and y+max_width <= BSIZE and max_width <= 5:
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
    # FIXME - 이것도, 고려 안해줬다. -> 모든 반례에 대해 하나씩 테스트해볼 것.
    max_width = find_largest_square(start_x, start_y)
    width = max_width
    # visited[r][c] == 1이기 때문에 max_width 리턴값은 항상 1 이상
    # if max_width > 0:
    cur_cnt = -1
    while width >= 1:
        if cnt_left[width] == 0:
            width -= 1
            # if else문 너무 중첩되니까 헷갈려서 continue로 처리했다.
            continue
        
        cnt_left[width] -= 1
        cover(start_x, start_y, width)
        next_pos = next_fill(visited)
        
        if next_pos == (-1, -1):
            cnt_left[width] += 1
            # 세상에. 이런 실수를?
            # uncover(r, c, width)
            uncover(start_x, start_y, width)
            return cnt + 1
        
        # 항상 채워야 할(아직 1인) 칸만 solution 함수에 입력해야 함
        res = solution(next_pos[0], next_pos[1], cnt+1)
        
        # 재귀함수니까 다시 visited 해제해주어야 함
        cnt_left[width] += 1
        uncover(start_x, start_y, width)
        width -= 1
        
        # 현재 width 이하로는 유효하지 않다는 뜻
        if res == -1:
            # FIXME - width == max_width 이었다고 해서 바로 -1 불가능하다고 판단하면 안된다.
            # if width == max_width:
            #     return -1
            continue
        
        # 현재까지의 cnt : cnt, 앞으로의 cnt : res(res는 여기서 -1이 아닌 유효한 값인 경우만)
        if cur_cnt == -1 or cur_cnt > res:
            cur_cnt = res
        elif cur_cnt <= res:
            break
        
    
    return cur_cnt


start_x = -1
start_y = -1
for r in range(BSIZE):
    for c in range(BSIZE):
        if board[r][c] == 1:
            start_x, start_y = r, c
            break
    if (start_x, start_y) != (-1, -1):
        break

if (start_x, start_y) != (-1, -1):
    print(solution(start_x, start_y, 0))
else:
    print(0)
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [['']*W for _ in range(H)]
for r in range(H):
    row = input().rstrip('\n')
    for c in range(W):
        board[r][c] = row[c]


# 동, 서, 남, 북
dx = [0,  0, 1, -1]
dy = [1, -1, 0,  0]

# NOTE: 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.
# 그리 간단한 문제가 아닌 듯
'''
왼쪽으로 이동하고자 할때, 우선 R과 B의 순서를 파악한 다음 그 순서대로 이동시켜야 한다.
만약 RB 이렇게 있다면 오른쪽(동쪽)으로 이동 시 B가 먼저 끝으로 이동, 그 다음에 R을 이동
왼쪽으로 이동 시 R이 왼쪽으로 먼저 끝으로 이동, 그 다음에 B를 이동.
''' 

def is_blue_ahead(red_loc, blue_loc, dir):
    x, y = red_loc
    mx, my = x+dx[dir], y+dy[dir]
    while board[mx][my] != '#':
        if (mx, my) == blue_loc:
            return True
        elif board[mx][my] == 'O':
            return False
        mx += dx[dir]
        my += dy[dir]
    return False



def move(start_loc, dir):
    x, y = start_loc
    mx, my = x+dx[dir], y+dy[dir]
    
    while board[mx][my] != '#':
        if board[mx][my] == 'O':
            return (mx, my)
        elif board[mx][my] == '.':
            mx += dx[dir]
            my += dy[dir]
        # 다른 공을 만난 경우
        else:
            break
    
    return (mx-dx[dir], my-dy[dir])


def update_board(ball, prev_loc, curr_loc):
    board[prev_loc[0]][prev_loc[1]] = '.'
    board[curr_loc[0]][curr_loc[1]] = ball


def solution(red_loc, blue_loc, visited, cnt):
    if cnt == 10:
        return -1
    
    answer = -1
    for move_dir in range(4):
        # red가 가는 길 중간에 blue가 있다면, blue를 먼저 이동시켜야 한다.
        if is_blue_ahead(red_loc, blue_loc, move_dir):
            moved_blue_loc = move(blue_loc, move_dir)
            # blue_loc == (-1, -1)인 건 실패이므로 일단 건너뛴다(continue)
            if blue_loc != hole:
                update_board('B', blue_loc, moved_blue_loc)
                moved_red_loc = move(red_loc, move_dir)
                if moved_red_loc == hole:
                    return cnt+1
                if (moved_red_loc, moved_blue_loc) in visited:
                    update_board('B', moved_blue_loc, blue_loc)
                    continue
                visited.add((moved_red_loc, moved_blue_loc))
                tmp = solution(moved_red_loc, moved_blue_loc, visited, cnt+1)
                # 그리고 다시 visited를 해제, 이동을 다시 원래 위치로
                visited.remove((moved_red_loc, moved_blue_loc))
                update_board('B', moved_blue_loc, blue_loc)
                update_board('R', moved_red_loc, red_loc)
                if tmp != -1:
                    if answer == -1 or answer > tmp:
                        answer = tmp
                
        else:
            moved_red_loc = move(red_loc, move_dir)
            if moved_red_loc == hole:
                update_board('R', red_loc, moved_red_loc)
                board[hole[0]][hole[1]] = 'O'
                moved_blue_loc = move(blue_loc, move_dir)
                if moved_blue_loc != hole:
                    return cnt+1
                else:
                    update_board('R', moved_red_loc, red_loc)
                    board[hole[0]][hole[1]] = 'O'
            
            else:
                update_board('R', red_loc, moved_red_loc)
                moved_blue_loc = move(blue_loc, move_dir)
                if moved_blue_loc == (-1, -1):
                    update_board('R', moved_red_loc, red_loc)
                else:
                    if (moved_red_loc, moved_blue_loc) in visited:
                        update_board('R', moved_red_loc, red_loc)
                        continue
                    visited.add((moved_red_loc, moved_blue_loc))
                    update_board('B', blue_loc, moved_blue_loc)
                    tmp = solution(moved_red_loc, moved_blue_loc, visited, cnt+1)
                    # 이동을 다시 원래 위치로
                    visited.remove((moved_red_loc, moved_blue_loc))
                    update_board('B', moved_blue_loc, blue_loc)
                    update_board('R', moved_red_loc, red_loc)
                    if tmp != -1:
                        if answer == -1 or answer > tmp:
                            answer = tmp
    
    return answer


for r in range(H):
    for c in range(W):
        if board[r][c] == 'R':
            red_loc = (r, c)
        if board[r][c] == 'B':
            blue_loc = (r,c)
        if board[r][c] == 'O':
            hole = (r,c)

visited = set()
visited.add((red_loc, blue_loc))
print(solution(red_loc, blue_loc, visited, 0))

'''
반례: https://www.acmicpc.net/board/view/110513
10 7
#######
#.....#
#.B...#
#R....#
#.....#
#.....#
#...O.#
#.....#
#.....#
#######
'''
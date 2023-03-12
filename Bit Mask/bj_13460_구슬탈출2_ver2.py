import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = []
for r in range(H):
    row = input().rstrip('\n')
    board.append(list(s for s in row))


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
                # NOTE - R에 대해서도 update_board 해줘야 하는데 안했다.
                update_board('R', red_loc, moved_red_loc)
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
                # NOTE - blue가 hole에 빠지게 되는 경우를 (-1,-1)에서 hole로 고쳤어야 했는데... 기존 레가시 코드를 그대로 놔두고
                # 위에만 업데이트한 결과다.
                # if moved_blue_loc == (-1, -1):
                if moved_blue_loc == hole:
                    update_board('R', moved_red_loc, red_loc)
                    board[hole[0]][hole[1]] = 'O'
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
반례:
10 10
##########
#RB....#.#
#..#.....#
#........#
#.O......#
#...#....#
#........#
#........#
#.......##
##########
정답: 10
출력: -1
'''

'''
여전히 23%에서 틀리는데 반례 찾았다.
7 8
########
#.#.#.##
########
#...#..#
#.OBR..#
##.##..#
########
정답: 2
출력: 1
'''

# 현재 hole (O)이 board에서 사라지는 문제
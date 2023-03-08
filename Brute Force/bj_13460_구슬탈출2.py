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



def move(ball, start_loc, dir, visited):
    x, y = start_loc
    path = []
    
    mx, my = x+dx[dir], y+dy[dir]
    
    if ball == 'R':
        while board[mx][my] != '#' and not visited[mx][my]:
            if board[mx][my] == 'O':
                return (-1, -1), path
            elif board[mx][my] == '.':
                visited[mx][my] = True
                mx += dx[dir]
                my += dy[dir]
                path.append((mx, my))
            # 다른 공을 만난 경우
            else:
                break
    # is_red == False, 즉 blue면 visied 배열을 참조, 변경하면 X
    elif ball == 'B':
        while board[mx][my] != '#':
            if board[mx][my] == 'O':
                return (-1, -1), path
            elif board[mx][my] == '.':
                mx += dx[dir]
                my += dy[dir]
            # 다른 공을 만난 경우
            else:
                break
    
    return (mx-dx[dir], my-dy[dir]), path
        

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
            moved_blue_loc, _ = move('B', blue_loc, move_dir, visited)
            # blue_loc == (-1, -1)인 건 실패이므로 일단 건너뛴다(continue)
            if blue_loc != (-1, -1):
                update_board('B', blue_loc, moved_blue_loc)
                moved_red_loc, path = move('R', red_loc, move_dir, visited)
                if moved_red_loc == (-1, -1):
                    return cnt+1
                # R, B 둘다 가만히 제자리에 있는 경우는 제외해야 한다.
                if not (moved_red_loc == red_loc and moved_blue_loc == blue_loc):
                    tmp = solution(moved_red_loc, moved_blue_loc, visited, cnt+1)
                    # 그리고 다시 visited를 해제
                    for x,y in path:
                        visited[x][y] = False
                    # 이동을 다시 원래 위치로
                    update_board('B', moved_blue_loc, blue_loc)
                    update_board('R', moved_red_loc, red_loc)
                    if tmp != -1:
                        if answer == -1 or answer > tmp:
                            answer = tmp
            else:
                update_board('B', moved_blue_loc, blue_loc)
                
        else:
            moved_red_loc, path = move('R', red_loc, move_dir, visited)
            if moved_red_loc == (-1, -1):
                return cnt+1
            # 이 사이에 red_loc도 board에 업데이트해야 함
            update_board('R', red_loc, moved_red_loc)
            moved_blue_loc, _ = move('B', blue_loc, move_dir, visited)
            if moved_blue_loc == (-1, -1):
                for x,y in path:
                    visited[x][y] = False
                update_board('R', moved_red_loc, red_loc)
            else:
                update_board('B', blue_loc, moved_blue_loc)
                if not (moved_red_loc == red_loc and moved_blue_loc == blue_loc):
                    tmp = solution(moved_red_loc, moved_blue_loc, visited, cnt+1)
                    # 이동을 다시 원래 위치로
                    update_board('B', moved_blue_loc, blue_loc)
                    update_board('R', moved_red_loc, red_loc)
                    for x,y in path:
                        visited[x][y] = False
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

visited = [[False]*W for _ in range(H)]
visited[red_loc[0]][red_loc[1]] = True
# blue는 visited 갱신 X
# visited[blue_loc[0]][blue_loc[1]] = True
print(solution(red_loc, blue_loc, visited, 0))
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

H, W, D = map(int, input().split())
board = [ list(map(int, input().split()) ) for _ in range(H) ]


def bfs(vertical_dist, current_row, archer_pos):
    
    # 적의 x 좌표 위치를 0으로(상대적 위치)
    enemy_x = 0
    
    # down, left, right
    dx = [1, 0,  0]
    dy = [0, -1, 1]
    
    cnt_killed = 0
    visited_archer_pos = []
    
    # REVIEW - 이런 모호한 네이밍은 금지
    # for y in current_row:
    for y in range(W):
        # y == 1 즉 적이 있을 때나 아직 활을 못 쏜 궁수가 남아있을 때만 실행
        if current_row[y] == 0 or len(visited_archer_pos) == 3:
            continue
        
        curr_move = 0
        q = deque([((enemy_x, y), curr_move) ])
        # vertical_dist: 적으로부터 궁수까지의 행(세로) 거리
        visited = [[False]*W for _ in range(vertical_dist+1)]
        visited[enemy_x][y] = True

        while q:
            (curr_x, curr_y), curr_move = q.popleft()
            
            # FIXME - WRONG
            # if curr_move > D:
            #     break
            if curr_move >= D:
                break
            
            for i in range(3):
                moved_x, moved_y = curr_x+dx[i], curr_y+dy[i]
                #FIXME - 여기서 더하는 게 아니라
                # curr_cnt += 1
                if (0 <= moved_x <= vertical_dist and 0 <= moved_y < W) and not visited[moved_x][moved_y]:
                    visited[moved_x][moved_y] = True
                    
                    if moved_x == vertical_dist and moved_y in archer_pos \
                        and moved_y not in visited_archer_pos:
                        visited_archer_pos.append(moved_y)
                        # 적(1)을 제거(0으로 변환)
                        cnt_killed += 1
                        current_row[y] = 0
                        break
                    else:
                        q.append(((moved_x, moved_y), curr_move+1 ) )
            if current_row[y] == 0:
                break
    
    # FIXME - visited_archer_pos의 크기를 반환하는 게 아니라 1에서 0으로 변한 개수
    # return current_row, len(visited_archer_pos)
    
    return current_row, cnt_killed
        

answer = 0
cnt_enemies = sum(sum(row) for row in board)

for archer_y_coord in combinations(range(W), 3):
    # 안해주면 다음 iteration 때 무용지물
    board_copy = [row.copy() for row in board]
    curr_answer = 0
    
    for turn in range(H+1-D):
        for r in range(H-1, H-D-1, -1):
            curr_row = board_copy[r-turn]
            # vertical_distance : 적과 궁수의 x(행, 세로를 말한다) 좌표 차이
            vertical_distance = H - r
            updated_row, cnt_enemy_killed = bfs(vertical_distance, curr_row, archer_y_coord)
            
            board_copy[r-turn] = updated_row
            curr_answer += cnt_enemy_killed
    
    answer = max(answer, curr_answer)
    if answer == cnt_enemies:
        break

print(answer)

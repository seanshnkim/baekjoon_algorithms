import sys
input = sys.stdin.readline
from itertools import combinations

H, W, D = map(int, input().split())
board = [ list(map(int, input().split()) ) for _ in range(H) ]
cnt_enemies = sum(sum(row) for row in board)

# input: curr_row, vertical_dist, available_archer_pos(남은 궁수 수) 
# return: curr_row, available_arch_pos both updated
def update_row(curr_row, vertical_dist, available_archer_pos):
    killed_enemies_y = set()
    finished_archers_y = []
    
    for arc in available_archer_pos:
        killed_by_archer = False
        # 문제 조건:
        ############
        # 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 
        # 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 
        # 같은 적이 여러 궁수에게 공격당할 수 있다.
        ############
        # archer y (가로) 위치를 기준으로 왼쪽으로 탐색
        for y in range(arc, -1, -1):
            dist = vertical_dist + abs(y-arc)
            if y < 0 or dist > D:
                break
            if curr_row[y] == 1:
                killed_enemies_y.add(y)
                killed_by_archer = True
                finished_archers_y.append(arc)
                break
        if not killed_by_archer:
            # 오른쪽으로 탐색
            for y in range(arc+1, W):
                dist = vertical_dist + abs(y-arc)
                if y >= W or dist > D:
                    break
                if curr_row[y] == 1:
                    killed_enemies_y.add(y)
                    killed_by_archer = True
                    finished_archers_y.append(arc)
                    break
    
    for y in list(killed_enemies_y):
        curr_row[y] = 0
    for y in finished_archers_y:
        available_archers.remove(y)
    
    return curr_row, available_archer_pos


answer = 0
for archer_y_pos in combinations(range(W), 3):
    tmp_board = [row.copy() for row in board]
    
    #FIXME - D의 크기에 상관없이 turn은 H의 크기와 같다
    # for turn in range(H-D+1):
    for turn in range(H):
        available_archers = list(archer_y_pos)
        
        up_limit = max(-1, H-1-turn-D)
        for r in range(H-1-turn, up_limit, -1):
            if not available_archers:
                break
            curr_row = tmp_board[r]
            x_dist = H - (r+turn)
            
            upd_row, upd_arc_pos = update_row(curr_row, x_dist, available_archers)
            
            tmp_board[r] = upd_row
            available_archers = upd_arc_pos
    
    num_killed = cnt_enemies - sum(sum(row) for row in tmp_board)
    answer = max(answer, num_killed)
    
    if answer == cnt_enemies:
        break
    
print(answer)


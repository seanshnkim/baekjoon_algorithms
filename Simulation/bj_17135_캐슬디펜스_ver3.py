import sys
input = sys.stdin.readline
from itertools import combinations

H, W, D = map(int, input().split())
board = [ list(map(int, input().split()) ) for _ in range(H) ]
cnt_enemies = sum(sum(row) for row in board)

# input: curr_row, vertical_dist, available_archer_pos(남은 궁수 수) 
# return: curr_row, available_arch_pos both updated
def update_row(curr_row, vertical_dist, available_archer_pos):
    left_archers = set(available_archer_pos)
    
    for arc in available_archer_pos:
        # 문제 조건:
        ############
        # 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 
        # 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 
        # 같은 적이 여러 궁수에게 공격당할 수 있다.
        ############
        # move : arc(궁수 y 좌표)를 기준으로 (양방향으로) 움직이는 칸 수
        for move in range(W):
            if (vertical_dist + move > D) or len(left_archers) == 0:
                break
            # 왼쪽 먼저 탐색해야 함
            moved = arc-move
            if moved >= 0 and curr_row[moved] == 1:
                left_archers.remove(arc)
                curr_row[moved] = 0
                # 궁수 사용했으니까 for loop break
                break
            # 오른쪽
            moved = arc+move
            if moved < W and curr_row[moved] == 1:
                left_archers.remove(arc)
                curr_row[moved] = 0
                # 궁수 사용했으니까 for loop break
                break
    
    return curr_row, list(left_archers)


answer = 0
for archer_y_pos in combinations(range(W), 3):
    tmp_board = [row.copy() for row in board]
    available_archers = list(archer_y_pos)
    
    #FIXME - D의 크기에 상관없이 turn은 H의 크기와 같다
    # for turn in range(H-D+1):
    for turn in range(H):
        
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


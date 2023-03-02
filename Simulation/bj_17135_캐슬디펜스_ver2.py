import sys
input = sys.stdin.readline
from itertools import combinations

H, W, D = map(int, input().split())
board = [ list(map(int, input().split()) ) for _ in range(H) ]
cnt_enemies = sum(sum(row) for row in board)

# input: curr_row, vertical_dist, available_archer_pos(남은 궁수 수) 
# return: curr_row, available_arch_pos both updated
def update_row(curr_row, vertical_dist, available_archer_pos):
    for y in range(W):
        if not available_archer_pos:
            break
        elif curr_row[y] == 1:
            for arc in available_archer_pos:
                dist = vertical_dist + abs(arc-y)
                if dist <= D:
                    # archer(궁수) 수는 3이기 때문에 remove 메서드의 시간복잡도는 무시할 수준
                    available_archer_pos.remove(arc)
                    curr_row[y] = 0
                    break
                    
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


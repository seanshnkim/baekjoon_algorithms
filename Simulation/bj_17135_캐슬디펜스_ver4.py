import sys
input = sys.stdin.readline
from itertools import combinations

H, W, D = map(int, input().split())
board = [ list(map(int, input().split()) ) for _ in range(H) ]
cnt_enemies = sum(sum(row) for row in board)


def kill_by_turn(cur_board, start_row, arc_pos):
    left_archers = set(arc_pos)
    killed_enemies = set()
    
    for d in range(D):
        if start_row-d < 0:
            break
        
        cur_row = cur_board[start_row-d]
        
        if not left_archers:
            break
        for arc in arc_pos:
            if arc not in left_archers:
                continue
            for move in range(0, D-d):
                if arc-move >= 0 and cur_row[arc-move] == 1:
                    left_archers.remove(arc)
                    killed_enemies.add( (start_row-d, arc-move) )
                    break
                if arc+move < W and cur_row[arc+move] == 1:
                    left_archers.remove(arc)
                    killed_enemies.add( (start_row-d, arc+move) )
                    break
    return killed_enemies


answer = 0
for archers_y in combinations(range(W), 3):
    # tmp_board = board.copy()
    tmp_board = [row.copy() for row in board]
    cnt_killed = 0
    for turn in range(H):
        enemies = kill_by_turn(tmp_board, H-1-turn, archers_y)
        cnt_killed += len(enemies)
        
        for enemy in enemies:
            tmp_board[enemy[0]][enemy[1]] = 0
            
    answer = max(answer, cnt_killed)

print(answer)
'''
반례: 
5 5 2
1 0 1 1 1
0 1 1 1 1
1 0 1 0 1
1 1 0 1 0
1 0 1 0 1
정답: 14
출력: 15
'''
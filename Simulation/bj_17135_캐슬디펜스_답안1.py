import sys
input = sys.stdin.readline

n,m,d = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

selected = []

def find_nearest(archor_pos, enemy_pos):
    deleted_enemy = set()
    for a_y, a_x in archor_pos:
        tmp_result = (100,(0,0))
        for e_y, e_x in enemy_pos:
            tmp_distance = abs(a_y-e_y) + abs(a_x-e_x)
            if tmp_distance > d:
                continue
            if tmp_result[0] > tmp_distance:
                tmp_result = (tmp_distance, (e_y,e_x))
            elif tmp_result[0] == tmp_distance and tmp_result[1][1] > e_x:
                tmp_result = (tmp_distance, (e_y,e_x))
        # print(tmp_result)
        if tmp_result[0] == 100:
            continue
        deleted_enemy.add(tmp_result[1])
    return deleted_enemy
    # print(deleted_enemy, archor_pos)
                

        


def find_enemies(board):
    enemies = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                enemies.append((r,c))
    return enemies


def simulation(selected):
    global board
    copy_board = [board[i][::] for i in range(n)]
    archor_pos = [(n,i) for i in (selected)]
    enemy_pos = set(find_enemies(copy_board))
    count = 0
    for i in range(n):
        deleted_enemy = find_nearest(archor_pos, enemy_pos)
        count += len(deleted_enemy)
        for enemy in deleted_enemy:
            enemy_pos.remove(enemy)
        tmp_enemy_pos = set()
        for enemy in enemy_pos:
            if enemy[0] == n-1:
                continue
            tmp_enemy_pos.add((enemy[0]+1, enemy[1]))
        enemy_pos = tmp_enemy_pos
    return count



    # print(archor_pos)
    # print(selected)

answer = 0
def dfs(l,s):
    global selected
    global answer
    # print(l,s)
    if l == 3:
        answer = max(answer,simulation(selected))
        # print(selected)
        # print()
        return
    
    for i in range(s, m-(3-(l+1))):
        selected.append(i)
        dfs(l+1, i+1)
        selected.pop()

dfs(0,0)
print(answer)

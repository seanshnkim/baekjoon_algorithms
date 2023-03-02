import sys
input = sys.stdin.readline

S, N_print = input().split()
N_print.rstrip('\n')
S = int(S)

'''
디지털 숫자 8을 기준으로,
0 -> 맨 위 가로
1 -> 왼쪽 위 세로
2 -> 오른쪽 위 세로
3 -> 중간 가로
4 -> 왼쪽 아래 세로
5 -> 오른쪽 아래 세로
6 -> 맨 아래 가로
를 그린다
'''
def draw_stroke(idx):
    line = ''
    locations = []
    
    if idx == 0:
        line = '-'
        for i in range(1, S+1):
            locations.append((0, i) )
    elif idx == 1:
        line = '|'
        for i in range(1, S+1):
            locations.append((i, 0) )
    elif idx == 2:
        line = '|'
        for i in range(1, S+1):
            locations.append((i, S+1) )
    elif idx == 3:
        line = '-'
        for i in range(1, S+1):
            locations.append((S+1, i) )
    elif idx == 4:
        line = '|'
        for i in range(S+2, 2*S+2):
            locations.append((i, 0) )
    elif idx == 5:
        line = '|'
        for i in range(S+2, 2*S+2):
            locations.append((i, S+1) )
    else:
        line = '-'
        for i in range(1, S+1):
            locations.append((2*S+2, i) )
    
    return line, locations

stroke_locations_by_number = [
    # 0
    [0,1,2,4,5,6],
    # 1
    [2,5],
    # 2
    [0,2,3,4,6],
    # 3
    [0,2,3,5,6],
    # 4
    [1,2,3,5],
    # 5
    [0,1,3,5,6],
    # 6
    [0,1,3,4,5,6],
    # 7
    [0,2,5],
    # 8
    [0,1,2,3,4,5,6],
    # 9
    [0,1,2,3,5,6]
]

def make_num_board(num):
    board = [[' ']*(S+2) for _ in range(2*S+3)]
    
    order = stroke_locations_by_number[num]
    
    for ord in order:
        which_stroke, locations = draw_stroke(ord)
        for loc in locations:
            board[loc[0]][loc[1]] = which_stroke
    
    return board

# entire_board = []*(2*S+3)
entire_board = [[] for _ in range(2*S+3)]
for num_str in N_print:
    curr_num_board = make_num_board(int(num_str))
    
    for r in range(2*S+3):
        # 아주 처음(맨 왼쪽)에는 공백을 추가할 필요 없다.
        # 공백은 숫자 사이에만 추가하면 된다.
        # 줄(entire_board[r])이 비어있지 않을 때만:
        if entire_board[r]:
            entire_board[r].append(' ')
        entire_board[r].extend(curr_num_board[r])

# for row in entire_board:
#     print(*row)
for row in entire_board:
    print(''.join(row))

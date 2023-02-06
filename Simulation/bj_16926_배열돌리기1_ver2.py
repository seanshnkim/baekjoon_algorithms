import sys
input = sys.stdin.readline

H, W, n_rotate = map(int, input().split())
input_board = [list(map(int, input().split())) for _ in range(H)]

rotate_groups = []
n_group = min(H, W) // 2

for g_idx in range(n_group):
    group = []
    for j in range(g_idx, W-g_idx):
        # 맨 윗줄 전체(왼쪽에서 오른쪽으로 append)
        group.append(input_board[g_idx][j])
        
    for i in range(g_idx+1, H-g_idx-1):
        # 맨 오른쪽 줄(맨윗줄 제외, 위에서 아래로 append)
        group.append(input_board[i][W-g_idx-1])
        
    for j in range(W-g_idx-1, g_idx, -1):
        # 맨 아랫줄(맨 왼쪽 제외, 오른쪽에서 왼쪽으로 append)
        group.append(input_board[H-g_idx-1][j])
        
    for i in range(H-g_idx-1, g_idx, -1):
        # 맨 왼쪽 줄(맨 윗줄 제외, 아래에서 위로 append)
        group.append(input_board[i][g_idx])
        
    rotate_groups.append(group)


for g_idx in range(n_group):
    curr_group = rotate_groups[g_idx]
    len_group = len(curr_group)
    
    # 실제 이동하면 되는 횟수: rotate_idx
    rotate_idx = n_rotate % len_group
    
    for j in range(g_idx, W-g_idx):
        # 맨 윗줄 중 맨 왼쪽을 제외한 칸부터
        input_board[g_idx][j] = curr_group[rotate_idx]
        # 항상 나머지 연산은 해줘야 (rotate_idx의 범위는 0 이상 len_group 미만)
        rotate_idx = (rotate_idx+1) % len_group
        
    for i in range(g_idx+1, H-g_idx-1):
        input_board[i][W-g_idx-1] = curr_group[rotate_idx]
        rotate_idx = (rotate_idx+1)%len_group
        
    for j in range(W-g_idx-1, g_idx, -1):
        input_board[H-g_idx-1][j] = curr_group[rotate_idx]
        rotate_idx = (rotate_idx+1)%len_group
        
    for i in range(H-g_idx-1, g_idx, -1):
        input_board[i][g_idx] = curr_group[rotate_idx]
        rotate_idx = (rotate_idx+1)%len_group

for row in input_board:
    print(' '.join(map(str, row)))
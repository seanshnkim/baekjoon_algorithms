import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]


def in_board(x, y):
    return 0 <= x < N and 0 <= y < N


def bfs(min_val, max_val):
    start_val = board[0][0]
    if not (min_val <= start_val <= max_val):
        return False
    
    visited = [[False]*N for _ in range(N)]
    q = deque([(0,0) ])
    visited[0][0] = True
    
    while q:
        curr_x, curr_y = q.popleft()
        
        for i in range(4):
            moved_x, moved_y = (curr_x + dx[i]), (curr_y + dy[i])
            if in_board(moved_x, moved_y):
                if not visited[moved_x][moved_y] and \
                (min_val <= board[moved_x][moved_y] <= max_val):
                    q.append((moved_x, moved_y) )
                    visited[moved_x][moved_y] = True
        
    return visited[N-1][N-1]


left = 0
right = 200
while left <= right:
    mid = (left+right) // 2
    
    for min_val in range(0, 200-mid+1):
        # 한번이라도 성공한다면 break하고 바로 right 값을 업데이트
        if bfs(min_val, min_val+mid):
            right = mid-1
            break
    if right != mid-1:
        left = mid+1

# 예를 들어 답이 3이어도, right = mid(3)-1으로 한번 더 업데이트하고 while left <= right을
# 빠져나오므로 (left = 3, right = 2) -> left가 맞다
print(left)
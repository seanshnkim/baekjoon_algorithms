import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]

dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]


def in_board(x, y):
    return 0 <= x < N and 0 <= y < N


left = 0
right = 200

while left <= right:
    mid = (left+right) // 2
    
    # visited 배열 다시 초기화
    visited = [[False]*N for _ in range(N)]
    
    # 항상 deque 초기화할 때 실수... 얘는 생성자가 원래 튜플이나 리스트를 원소로 받아들이기 때문에
    # 튜플을 아이템으로 하는 deque 생성하려면 한번 더 리스트로 씌워줘야 함
    # q = deque((0, 0) )
    q = deque([(0,0) ] )
    visited[0][0] = True
    curr_min = curr_max = board[0][0]

    while q:
        curr = q.popleft()
        
        for i in range(4):
            moved_x = curr[0] + dx[i]
            moved_y = curr[1] + dy[i]
            if in_board(moved_x, moved_y) and not visited[moved_x][moved_y]:
                curr_val = board[moved_x][moved_y]
                if curr_val < curr_min:
                    score = curr_max - curr_val
                    if score <= mid:
                        visited[moved_x][moved_y] = True
                        q.append((moved_x, moved_y) )
                        curr_min = curr_val
                        
                elif curr_val > curr_max:
                    # 이렇게 되면 실제로 선택하지 않은 경로라 하더라도 최댓값은 취하게 돼서 오류가 생긴다.
                    # curr_max = curr_val
                    score = curr_val - curr_min
                    if score <= mid:
                        visited[moved_x][moved_y] = True
                        q.append((moved_x, moved_y) )
                        curr_max = curr_max
                
                else:
                    visited[moved_x][moved_y] = True
                    q.append((moved_x, moved_y) )

    # socre 값(mid)이 너무 작아서 도달도 못했다는 것 -> score 값을 높여줘야 함
    if not visited[N-1][N-1]:
        left = mid+1
    else:
        right = mid-1

# 최솟값을 구하는 문제이기 때문에 
# print(left)

# 이 코드의 반례:
'''
5
5 5 5 0 0
5 0 5 0 0
5 0 4 0 0
5 0 5 5 8
5 5 7 0 5
output : 4
answer : 3
'''
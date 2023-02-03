import sys
from collections import deque

dx = [-1, -2, -2, -1, 1, 2,  2,  1]
dy = [-2, -1,  1,  2, 2, 1, -1, -2]

board = []


def bfs(q):
    #REVIEW - 항상 q를 모두 비우고 bfs 함수가 종료하라는 법은 없다.
    while q:
        curr_loc = q.popleft()
        curr_depth = board[curr_loc[0]][curr_loc[1]]
        if curr_loc[0] == targ_r and curr_loc[1] == targ_c:
            return curr_depth
        
        for x,y in zip(dx, dy):
            r = curr_loc[0] + x
            c = curr_loc[1] + y
            
            if 0 <= r and r < width and 0 <= c and c < width:
                if r == targ_r and c == targ_c:
                    return curr_depth + 1
                elif board[r][c] == -1:
                    q.append((r, c))
                    board[r][c] = curr_depth + 1
    
    return curr_depth
    

n_test_case = int(sys.stdin.readline())
q = deque()
for _ in range(n_test_case):
    width = int(sys.stdin.readline())
    board = [[-1]*width for _ in range(width)]
    curr_r, curr_c = map(int, sys.stdin.readline().split())
    targ_r, targ_c = map(int, sys.stdin.readline().split())
    
    #FIXME - q.clear() 안해주면 문제 발생
    q.clear()
    q.append((curr_r, curr_c))
    board[curr_r][curr_c] = 0
    print(bfs(q))
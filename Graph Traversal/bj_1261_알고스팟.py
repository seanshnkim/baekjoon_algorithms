import sys
from collections import deque

'''
1. 빈방(0)이 있다면 거기로 간다.
2. 빈방이 아예 없다면 벽을 뚫는다.
3. 1,2번을 반복한다. 언제까지? 다음 좌표가 (N,M)이 될 때까지
'''

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

W, H = map(int, sys.stdin.readline().split())
board = []
for _ in range(H):
    row = sys.stdin.readline().rstrip('\n')
    board.append([int(i) for i in row])

cnts = [[-1]*W for _ in range(H)]
#REVIEW - 항상 초기값 설정해줘야 함!!
cnts[0][0] = 0

def bfs(q):
    while q:
        curr = q.popleft()
        for x,y in zip(dx, dy):
            r = curr[0]+x
            c = curr[1]+y
            
            if 0 <= r < H and 0 <= c < W:
                
                if   cnts[r][c] == -1 and board[r][c] == 0:
                    q.appendleft( (r, c) )
                    cnts[r][c] = cnts[curr[0]][curr[1]]
                elif cnts[r][c] == -1 and board[r][c] == 1:
                    q.append( (r, c) )
                    cnts[r][c] = cnts[curr[0]][curr[1]] + 1
                    
                if r == H-1 and c == W-1:
                    return cnts[r][c] 
                    
                    

# deque 생성할 때 항상 하는 실수:
# deque([n]) -> 정수 n을 원소로 갖는 덱의 생성
# deque의 첫 아이템을 튜플 또는 리스트로 넣으려면 다음과 같이 실행해야 함
q = deque([(0,0)])
print(bfs(q))

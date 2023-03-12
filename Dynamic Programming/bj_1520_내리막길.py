import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False]*W for _ in range(H)]

def solution(x, y):
    if x == H-1 and y == W-1:
        return 1
    
    answer = 0
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if (0 <= mx < H and 0 <= my < W) and board[mx][my] < board[x][y] and not visited[mx][my]:
            visited[mx][my] = True
            cur_cnt = solution(mx, my)
            visited[mx][my] = False
            
            if cur_cnt != -1:
                if answer == -1:
                    answer = cur_cnt
                else:
                    answer += cur_cnt
        
    return answer

# 답 출력
# cnt -> 1부터 시작하는 거 맞나>
visited[0][0] = True
print(solution(0, 0))
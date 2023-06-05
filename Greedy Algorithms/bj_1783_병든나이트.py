import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [[-1]*M for _ in range(N)]
visited[N-1][0] = 0

dx = [-2, -1, 1, 2]
dy = [ 1,  2, 2, 1]

ans = 1

# num -> 4자리의 4진수
def is_valid(num):
    path_set = set()
    for i in range(4):
        path_set.add(num & ( 3 << 2*i ))
    
    return path_set == set([0,1,2,3])


def dfs(x, y, move_cnt):
    global ans
    
    if move_cnt == 4:
        if not is_valid(visited[x][y]):
            visited[x][y] = -2
            return
        
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if 0 <= mx < N and 0 <= my < M and visited[mx][my] == -1:
            visited[mx][my] = visited[x][y] + i * (1 << 2*move_cnt)
            ans += 1
            dfs(x, y, move_cnt+1)
            

dfs(N-1, 0, 0)
print(ans)
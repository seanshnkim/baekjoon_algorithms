import sys
input = sys.stdin.readline
from collections import deque

N, *probs = map(int, input().split())
# 동서남북 순서로
probs = [prob*0.01 for prob in probs]
dx = [0,  0, 1, -1]
dy = [1, -1, 0,  0]
visited = [ [False]*(2*N+1) for _ in range(2*N+1) ]

cnt = 0
prob = 1
start = (N, N, cnt, prob)
visited[N][N] = True
q = deque([start])
answer = 0

while q:
    x, y, cnt, prob = q.popleft()
    
    if cnt == N:
        answer += prob
        continue
    
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if not visited[mx][my]:
            q.append( (mx, my, cnt+1, prob*probs[i]) )
            visited[mx][my] = True

print(answer)
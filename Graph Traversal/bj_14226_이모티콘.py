import sys
from collections import deque

# MAX_N = 1001
N = int(sys.stdin.readline())

# e: 현재 화면에 있는 이모티콘의 개수
# c: 현제 클립보드에 저장된 이모티콘의 개수
# visited[e][c] = minimum count(depth)
visited = [[-1]*(N+1) for _ in range(N+1)]
visited[1][0] = 0

def bfs(q):
    while q:
        curr = q.popleft()
        # e: 현재 화면에 있는 이모티콘의 개수
        # c: 현제 클립보드에 저장된 이모티콘의 개수
        e, c = curr[0], curr[1]
        
        # 모든 n(n>2)개의 이모티콘은 처음 1개 이모티콘에서 계속 복붙해서 2개,3개... 만들어 나갈 수 있기 때문
        # 따라서 visited[e][k]는 항상 e개보다 작거나 같다는 것이 보장되므로, e보다 클 때 탐색하는 건 의미가 없다.
        if e > 2 and visited[e][c] > e:
            continue
        
        next_steps = [[e+c, c], 
                      [e-1, c],
                      [e, e]]
        for next in next_steps:
            if 0 <= next[0] < N+1:
                if visited[next[0]][next[1]] == -1:
                        
                    visited[next[0]][next[1]] = visited[e][c] + 1
                    q.append(next)
    
    return min(i for i in visited[N] if i > -1)

q = deque([[1, 0]])
print(bfs(q))

with open('wrong_result.txt', 'w') as f:
    for n in range(N+1):
        f.write(str(min(i for i in visited[n] if i > -1)) + '\n')
import sys
from collections import deque
input = sys.stdin.readline

# H, W가 2차원 배열의 각 행, 열 크기라 하자
H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[False]*W for _ in range(H)]

# 가장 흔한 유형이 2차원 보드 내에서 상,하,좌,우로 움직이는 것.
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

# 시작 노드가 (0,0)이라고 한 건 단지 예시일 뿐. 문제 조건마다 다르겠지?
start = (0, 0,0)
# 목적지 노드에 다다르면 BFS 탐색을 멈추기로 가정하자. 이것도 문제 조건마다 다르다.
dest = (H-1, W-1)
# 먼저 시작 노드는 방문 처리를 해야 한다. 이거 실수로 빼먹지 않기
visited[start] = True

answer = 0
while q:
    cur_dist, x, y = q.popleft()

    if x == dest[0] and y == dest[1]:
        answer = cur_dist
        break

    for i in range(4):
        mx, my = x+dx[i], y+dy[i]

        if 0 <= mx < H and 0 <= my < W and not visited[mx][my]:
            q.append((cur_dist+1, mx, my))
            visited[mx][my] = True

# 여기선 시작점부터 목적지까지의 칸 이동 횟수(거리)를 리턴하지만
# 문제 조건마다 다른 값을 리턴하도록 설정할 수 있다.
print(answer)

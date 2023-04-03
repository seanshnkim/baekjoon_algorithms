from collections import deque

N_NUM = 1001
M_NUM = 101

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# way = [[0 for j in range(M_NUM)] for i in range(N_NUM)]
way = [[0]*N for _ in range(N)]
island = [[0]*N for _ in range(N)]
# island = [[0 for j in range(M_NUM)] for i in range(N_NUM)]

Q = deque()

for i in range(N):
    # row = list(map(int, input().split()))
    for j in range(N):
        # board[i][j] = row[j]
        if board[i][j] == 1:
            Q.append((i, j))
            way[i][j] = 0
        elif board[i][j] == 0:
            way[i][j] = -1

num_island = 0

for i in range(N):
    for j in range(N):
        if not board[i][j] or island[i][j] > 0:
            continue

        num_island += 1
        QI = deque()
        island[i][j] = num_island
        QI.append((i, j))

        while QI:
            x, y = QI.popleft()

            for d in range(4):
                mx, my = (x + dx[d], y + dy[d])

                if mx < 0 or my < 0 or mx >= N or my >= N:
                    continue

                if not board[mx][my] or island[mx][my] > 0:
                    continue

                island[mx][my] = num_island
                QI.append((mx, my))

bridge = N + N


while Q:
    x, y = Q.popleft()

    for d in range(4):
        mx, my = (x + dx[d], y + dy[d])

        if mx < 0 or my < 0 or mx >= N or my >= N:
            continue

        if island[mx][my] == island[x][y]:
            continue

        if island[mx][my] != 0:
            bridge = min(bridge, way[x][y] + way[mx][my])
            continue

        island[mx][my] = island[x][y]
        way[mx][my] = way[x][y] + 1
        Q.append((mx, my))

print(bridge)
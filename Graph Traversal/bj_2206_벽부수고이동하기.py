import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
# FIXME - 자료형 실수!!! 한참 헤맸다. 기록해두자.
# board = [[i for i in input()] for _ in range(H)]
board = [[int(i) for i in input().rstrip('\n')] for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0 , 0, 1, -1]

def bfs_with_wall(start_x, start_y, cnt_break):
    answer = -1
    # cnt_break = 0
    visited = [[False]*W for _ in range(H)]
    q = deque([(0, start_x, start_y)])
    visited[start_x][start_y] = True
    
    while q:
        d, x, y = q.popleft()
        
        if x == H-1 and y == W-1:
            if answer == -1 or answer > d:
                answer = d
            break
            
        is_move_possible = False
        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            
            if 0 <= mx < H and 0 <= my < W and not visited[mx][my]:
                if board[mx][my] == 0:
                    is_move_possible = True
                    q.append((d+1, mx, my))
                    visited[mx][my] = True
                    
        if not is_move_possible:
            if cnt_break > 0:
                return -1
            
            cnt_break += 1

            for i in range(4):
                mx, my = x+dx[i], y+dy[i]
                if 0 <= mx < H and 0 <= my < W and not visited[mx][my]:
                    board[mx][my] = 0
                    tmp = bfs_with_wall(mx, my, cnt_break=1)
                    if tmp != -1:
                        if answer == -1 or answer > d + tmp:
                            answer = d + tmp
                    board[mx][my] = 1
        
    return answer + 1
            
'''
맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
첫째 줄에 최단 거리 출력, 불가능하면 -1 출력
'''

# 경로가 없고 막혀있다면(즉 아직 (H, W)에 도착 X), 벽 하나를 부순다.
# 벽을 이미 1개 부순 상태에서 또 막히게 되면, -1을 리턴한다.
# 벽을 안 부수고 계속 이동할 수 있는 칸이 하나라도 있다면 그 칸으로 이동한다.
# 최종 경로를 구한다. 만약 최종 경로 중 벽을 한 칸 부수었다면 그대로 리턴,
# 벽을 한 칸도 부수지 않았다면 이번엔 벽을 한 칸만 부수어보면서 경로 탐색, 그 중에 더 작은 걸 리턴한다.
# 벽을 한 칸 부수어서 더 짧은 경로가 될 수 있는 경로라면, 해당 벽을 부수었을 때(그 벽의 위치를 (x, y)라 하자
# (1,1)부터 (x,y)까지의 경로와 (x,y)부터 (M,N)까지의 경로를 합친 결과가 더 짧아야 한다.

# 그리고 항상 경로 구하면 +1 더해주어야 한다(-1로 출력되는 결고 말고는)

'''
6 4
0100
1110
1000
0000
0111
0000
'''

print(bfs_with_wall(start_x=0, start_y=0, cnt_break=0))
import sys
input = sys.stdin.readline
from collections import namedtuple
Curve = namedtuple("Curve", ["s_x", "s_y", "s_orient", "gen"])

N_curve = int(input())
curves = [Curve(*map(int, input().split())) for _ in range(N_curve)]
visited = [[False]*101 for _ in range(101)]

'''0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
'''
dx = [1,  0, -1, 0]
dy = [0, -1,  0, 1]

# 세대가 하나씩 증가할 때마다 시계방향 90도 회전시켜서 확장하는 함수
# return: 추가된 점들(기존 점들도 포함해야 할까?), 다음 끝점
def rotate_expand(curr_points, end_point, start_point):
    end_x, end_y = end_point
    start_x, start_y = start_point
    added_points = []

    for point in curr_points:
        curr_x, curr_y = point
        
        rotated_x = end_x - (curr_y - end_y)
        rotated_y = end_y - (end_x - curr_x)
        
        added_points.append( (rotated_x, rotated_y) )
    
    # FIXME - 테스트 케이스만을 기준으로 계산, 착각!!
    # next_end_x = end_x + end_y
    # next_end_y = end_y - end_x
    next_end_x = end_x - (start_y - end_y)
    next_end_y = end_y - (end_x - start_x)
    
    return added_points, (next_end_x, next_end_y)


# 각 드래곤 커브를 주어진 세대까지 완성하는 함수
def make_curve(start_x, start_y, start_ori, generation):
    end_x = start_x + dx[start_ori]
    end_y = start_y + dy[start_ori]
    end_point = (end_x, end_y)
    
    start_point = (start_x, start_y)
    curr_points = [start_point, end_point]
    
    visited[start_x][start_y] = True
    visited[end_x][end_y] = True
    
    for _ in range(generation):
        added_points, next_end_p = rotate_expand(curr_points, end_point, start_point)
        curr_points.extend(added_points)
        
        for x,y in added_points:
            visited[x][y] = True
        
        end_point = next_end_p
    
    return


for i in range(N_curve):
    make_curve(curves[i].s_x, curves[i].s_y, curves[i].s_orient, curves[i].gen)

# 이제 격자판에 대해 검사
cnt_square = 0
for x in range(100):
    for y in range(100):
        if visited[x][y]   and visited[x+1][y] and \
           visited[x][y+1] and visited[x+1][y+1]:
               cnt_square += 1

print(cnt_square)
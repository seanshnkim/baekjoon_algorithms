import sys
input = sys.stdin.readline
from typing import List
from math import sqrt

coords = list(map(float, input().split()))
A_coord, B_coord, C_coord = coords[:3], coords[3:6], coords[6:9]

# C를 원점으로 평행이동 (그래도 거리는 같다)
for i in range(3):
    A_coord[i] -= C_coord[i]
    B_coord[i] -= C_coord[i]
C_coord = [0,0,0]


def dist(A_coord: List, B_coord: List) -> float:
    dist = 0
    for i in range(3):
        dist += (A_coord[i] - B_coord[i])*(A_coord[i] - B_coord[i])
    return sqrt(dist)


def dist_from_O(A_coord: List) -> float:
    return sqrt(sum(i*i for i in A_coord))


def coord_in_line(A_coord, B_coord, ratio_from_A):
    res = []
    for i in range(3):
        res.append(A_coord[i] + (B_coord[i] - A_coord[i])*ratio_from_A )
    return res


start = 0
end = 1
seg_len = dist(A_coord, B_coord)

while (end-start) > (10**(-6) / seg_len ):
    r_left = start + (end-start) / 3
    r_right = end - (end-start) / 3
    
    p_left = coord_in_line(A_coord, B_coord, r_left)
    p_right = coord_in_line(A_coord, B_coord, r_right)
    
    if dist_from_O(p_left) >= dist_from_O(p_right):
        start = r_left
    else:
        end = r_right
    #FIXME - 이게 들어가면 안된다! dist(p_left), dist(p_right)가 같아도 여전히 최솟값에 도달하지 않았을 수도 있다.
    # else:
    #     break

print(dist_from_O(p_left) )

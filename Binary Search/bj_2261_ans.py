import sys
from collections import namedtuple
input = sys.stdin.readline

Point = namedtuple('Point', ['x', 'y'])

N = int(input())
points = [Point(*map(int,input().split())) for _ in range(N)]
points.sort()


def dist_sqrd(p1: Point, p2: Point):
    return (p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y)


def brute_force(a, start, end):
    ans = -1
    for i in range(start, end):
        for j in range(i+1, end+1):
            d = dist_sqrd(a[i], a[j])
            if ans == -1 or ans > d:
                ans = d
    return ans


def solution(a, start, end):
    if end-start <= 2:
        return brute_force(a, start, end)
    
    mid = (start + end) // 2
    left = solution(a, start, mid)
    right = solution(a, mid+1, end)
    
    ans = min(left, right)
    
    to_search = []
    for i in range(start, end+1):
        x_diff = a[i].x - a[mid].x
        if x_diff*x_diff < ans:
            to_search += [a[i]]

    to_search.sort(key=lambda p: (p.y, p.x))
    
    for i in range(len(to_search)-1):
        for j in range(i+1, len(to_search)):
            y_diff = to_search[j].y - to_search[i].y
            if y_diff*y_diff < ans:
                curr_dist = dist_sqrd(to_search[i], to_search[j])
                ans = min(curr_dist, ans)
            else:
                break
    return ans


print(solution(points, 0, N-1))
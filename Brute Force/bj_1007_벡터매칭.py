import sys
input = sys.stdin.readline
from itertools import combinations
from math import sqrt

def len_vector(x, y):
    return sqrt(x*x + y*y)

T = int(input())
for _ in range(T):
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    sum_X = sum(p[0] for p in points)
    sum_Y = sum(p[1] for p in points)
    
    ans = float('inf')
    
    for comb in combinations(range(N), int(N//2)):
        pos_X = sum(points[i][0] for i in comb)
        pos_Y = sum(points[i][1] for i in comb)
        
        res_X, res_Y = 2*pos_X - sum_X, 2*pos_Y - sum_Y
        
        ans = min(ans, len_vector(res_X, res_Y))
    
    print(ans)
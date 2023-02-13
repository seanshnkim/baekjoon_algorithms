import sys
input = sys.stdin.readline
from math import sqrt

x, y, c = map(float, input().split())


def get_c(x, y, w):
    h1 = sqrt(x*x - w*w)
    h2 = sqrt(y*y - w*w)
    
    c = (h1 * h2) / (h1 + h2)
    return c


start = 0
end = min(x, y)

while end-start >= 10**(-3):
    mid = (start+end) / 2
    
    curr_c = get_c(x, y, mid)
    
    if curr_c > c:
        start = mid
    elif curr_c < c:
        end = mid
    else:
        break

print(mid)
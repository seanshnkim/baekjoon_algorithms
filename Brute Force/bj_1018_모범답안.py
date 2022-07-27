# 2022-06-27(June 27th, 2022), Sehyun Kim

import sys
from itertools import accumulate as acc
input = sys.stdin.readline

n, m = map(int, input().split())
y = [[0]*(m+1)]

for i in range(n):
    ac = [0]
    ac.extend(acc([((s=='W')+i+j) % 2 for j, s in enumerate(input().rstrip())]))
    print(f'y[-1]: {y[-1]}')
    y.append([k + j for k, j in zip(ac, y[-1])])

res = 32
for i in range(n-7):
    for j in range(m-7):
        u = y[i+8][j+8]-y[i+8][j]-y[i][j+8]+y[i][j]
        res = min(res, u, 64-u)
print(res)
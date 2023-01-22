import sys

E, S, M = map(int, sys.stdin.readline().split())
E_lim, S_lim, M_lim = 15, 28, 19

e = s = m = 1
cnt = 1
while not (E == e and S == s and M == m):
    cnt += 1
    e += 1
    s += 1
    m += 1
    if e > E_lim:
        e = 1
    if s > S_lim:
        s = 1
    if m > M_lim:
        m = 1

print(cnt)
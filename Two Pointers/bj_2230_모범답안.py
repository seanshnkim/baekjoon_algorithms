# 2022-07-27(July 27th, 2022), Sehyun Kim

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if M:
    ns = set()
    while N:
        N -= 1
        ns.add(int(input()))
    nl = sorted(list(ns))
    r = 2222222222
    i, j = 0, 1
    maxlen = len(nl)
    while j < maxlen:
        if nl[j] - nl[i] < M:
            j += 1
            if j == maxlen:
                break
        else:
            r = min(r, nl[j] - nl[i])
            i += 1
            if i == j:
                j += 1
    print(r)
else:
    print(0)
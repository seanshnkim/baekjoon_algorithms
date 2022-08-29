import sys

len_queue, n_select = map(int, sys.stdin.readline().split())
loc_list = list(map(int, sys.stdin.readline().split()))

q = [i for i in range(1, len_queue+1)]
res = 0

for loc in loc_list:
    for i in range(len(q)):
        if q[i] == loc:
            idx = i
            break
    f = idx
    r = len(q) - idx
    while q[0] != loc:
        q.append(q[0])
        del q[0]
    del q[0]
    # 이 부분이 핵심 (내 풀이에서는 부등호 조건 역할)
    res += min(f, r)

print(res)
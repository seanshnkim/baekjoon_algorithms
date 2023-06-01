import sys
input = sys.stdin.readline
import heapq

N = int(input())
q = []
for _ in range(N):
    p, d = map(int, input().split())
    heapq.heappush(q, (d, p))

res_q = []
len_res = 0
while q:
    cur_d, cur_p = heapq.heappop(q)
    if len_res == cur_d:
        if cur_p > res_q[0]:
            heapq.heappop(res_q)
            heapq.heappush(res_q, cur_p)
    else:
        heapq.heappush(res_q, cur_p)
        len_res += 1

print(sum(res_q))

import sys
input = sys.stdin.readline
import heapq

N = int(input())
q = []
for _ in range(N):
    p, d = map(int, input().split())
    heapq.heappush(q, (d, p))

ans = 0
prev_day = q[0][0]
daily_max_profit = 0

while q:
    cur_day = q[0][0]
    
    if cur_day == prev_day:
        cur_pair = heapq.heappop(q)
        daily_max_profit = max(daily_max_profit, cur_pair[1])
    else:
        prev_day = cur_day
        ans += daily_max_profit
        daily_max_profit = 0

last_day_profit = daily_max_profit
ans += last_day_profit
print(ans)
'''
반례:
10 1 10 1 300 2 300 2
'''

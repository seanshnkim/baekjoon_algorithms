import sys
input = sys.stdin.readline
import heapq

N = int(input())
q = []
# numbers = [int(input()) for _ in range(N)]
for _ in range(N):
    cur_num = int(input())
    heapq.heappush(q, cur_num)

ans = 0
while q:
    first = heapq.heappop(q)
    cur_sum = first
    
    if not q:
        break
    
    second = heapq.heappop(q)
    cur_sum += second
    heapq.heappush(q, cur_sum)
    ans += cur_sum

print(ans)
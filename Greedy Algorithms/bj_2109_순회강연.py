import sys
input = sys.stdin.readline
import heapq

N = int(input())

infos = []
for _ in range(N):
    p, d = map(int, input().split())
    heapq.heappush(infos, (-p, d))

ans = 0
time = 0

while infos:
    cur_p, cur_d = infos[0]
    
    if cur_d - time > 0:
        ans += (-1)*cur_p
        heapq.heappop(infos)
        time += 1
    else:
        heapq.heappop(infos)
    
    

print(ans)

import sys
input = sys.stdin.readline
import heapq

N = int(input())

infos = []
for _ in range(N):
    p, d = map(int, input().split())
    heapq.heappush(infos, (d, -p))

ans = 0
time = 0

while infos:
    cur_d, cur_p = heapq.heappop(infos)
    cur_p = (-1)*cur_p
    
    if cur_d - time > 0:
        cur_max = cur_p
        i = 0
        while infos and infos[0][0] == cur_d:
            next_p = infos[0][1]
            if next_p > cur_max:
                cur_max = next_p
            # i += 1
            heapq.heappop(infos)
        
        ans += cur_max
        time += 1
    
    else:
        break
    
    
print(ans)

'''
반례:
10 1 10 1 300 2 300 2
'''

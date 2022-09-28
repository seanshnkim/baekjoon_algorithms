from locale import currency
import sys
import heapq

N = int(sys.stdin.readline())

max_heap = []
for _ in range(N):
    curr_line = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        if len(max_heap) < N:
            heapq.heappush(max_heap, curr_line[i])
        else:
            heapq.heappushpop(max_heap, curr_line[i])

print(heapq.heappop(max_heap))




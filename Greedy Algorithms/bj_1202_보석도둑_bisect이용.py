import sys
input = sys.stdin.readline
from collections import namedtuple
import heapq
Jewel = namedtuple("Jewel", ["weight", "price"])

N_jewels, N_bags = map(int, input().split())

jewels = []
for _ in range(N_jewels):
    w, p = map(int, input().split())
    heapq.heappush(jewels, Jewel(weight=w, price=p) )
    
bags = [int(input()) for _ in range(N_bags)]
bags.sort()

answer = 0
curr_jewels = []
for bag in bags:
    if bag < jewels[0].weight:
        continue
    
    while jewels and bag >= jewels[0].weight:
        heapq.heappush(curr_jewels, (-1)*heapq.heappop(jewels).price)
    
    if curr_jewels:
        answer += (-1)*heapq.heappop(curr_jewels)
    elif not jewels:
        break
    # while jewels and bag >= jewels[0].weight:
    #     heapq.heappush(curr_jewels, (-1)*heapq.heappop(jewels).price)
    # if curr_jewels:
    #     answer += (-1)*heapq.heappop(curr_jewels)
    # elif not jewels:
    #     break

print(answer)


import sys
input = sys.stdin.readline
from collections import namedtuple
import bisect
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
for bag in bags:
    if bag < jewels[0].weight:
        continue
    upper_limit_j = bisect.bisect_right(jewels, (bag, 0))
    
    max_val = 0
    for i in range(upper_limit_j):
        curr_jewel = heapq.heappop(jewels)
        max_val = max(max_val, curr_jewel.price)
    
    answer += max_val

print(answer)


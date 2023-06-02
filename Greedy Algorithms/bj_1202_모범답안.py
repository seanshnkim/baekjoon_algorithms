import sys
input = sys.stdin.readline
from collections import namedtuple
import heapq

Jewel = namedtuple('Jewel', ['weight', 'value'])

num_jewel, num_bag = map(int, sys.stdin.readline().split())
jewels = []
for _ in range(num_jewel):
    w, v = map(int, input().split())
    jewels.append(Jewel(w, v))
jewels.sort(key=lambda x: x.weight, reverse=True)

bags = [int(input()) for _ in range(num_bag)]
bags.sort()

q = []
ans = 0

for i in range(num_bag):
    while jewels and bags[i] >= jewels[-1].weight:
        heapq.heappush(q, (-1)*jewels.pop().value)
    
    if q:
        ans += (-1)*heapq.heappop(q)

print(ans)
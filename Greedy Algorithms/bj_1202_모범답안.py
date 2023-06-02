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
jewels.sort(key=lambda x: x.weight)

bags = [int(input()) for _ in range(num_bag)]
bags.sort()

q = []
ans = 0
j_idx = 0

for i in range(num_bag):
    while j_idx < num_jewel and bags[i] >= jewels[j_idx].weight:
        heapq.heappush(q, (-1)*jewels[j_idx].value)
        j_idx += 1
    
    if q:
        ans += (-1)*heapq.heappop(q)

print(ans)
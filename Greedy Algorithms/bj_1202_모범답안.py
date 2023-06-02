import sys
input = sys.stdin.readline
from bisect import bisect_left
from collections import namedtuple

Jewel = namedtuple('Jewel', ['weight', 'value'])

num_jewel, num_bag = map(int, sys.stdin.readline().split())
jewels = []
for _ in range(num_jewel):
    w, v = map(int, input().split())
    jewels.append(Jewel(w, v))
jewels.sort(key=lambda x: x.value, reverse=True)

bags = [int(input()) for _ in range(num_bag)]
bags.sort()

ans = 0

for i in range(num_jewel):
    if num_bag == 0:
        break
    idx = bisect_left(bags, jewels[i].weight)
    if num_bag > 0 and idx < num_bag:
        ans += jewels[i].value
        bags.pop(idx)
        num_bag -= 1

print(ans)
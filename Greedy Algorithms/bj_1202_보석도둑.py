import sys
input = sys.stdin.readline
from collections import namedtuple
import bisect

Jewel = namedtuple("Jewel", ["weight", "price"])

N_jewels, N_bags = map(int, input().split())
jewels = [Jewel(*map(int, input().split())) for _ in range(N_jewels)]
bags = [int(input()) for _ in range(N_bags)]

jewels.sort(key=lambda x: (x.price, -x.weight), reverse=True)
bags.sort()

answer = 0
for j in jewels:
    if j.weight > bags[-1]:
        continue
    
    curr_idx = bisect.bisect_right(bags, j.weight)
    if bags:
        answer += j.price
        if curr_idx == 0:
            bags.pop(curr_idx)
        else:
            bags.pop(curr_idx-1)
    else:
        break

print(answer)
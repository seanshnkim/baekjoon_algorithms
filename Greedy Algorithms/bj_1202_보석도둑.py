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
    
    # bisect의 원리를 몰라서 틀림 -> 같아도 bisect_right는 같은 원소들 맨 오른쪽에 배치
    # curr_idx = bisect.bisect_right(bags, j.weight)
    curr_idx = bisect.bisect_left(bags, j.weight)
    if bags:
        answer += j.price
        bags.pop(curr_idx)

print(answer)

import sys
input = sys.stdin.readline
from collections import namedtuple
Flower = namedtuple("Flower", ["start", "end"])

FIXED_START = 301
FIXED_END = 1130

N = int(input())
flowers = []
for _ in range(N):
    dates = list(input().split())
    dates = ['0'+d if len(d) == 1 else d for d in dates]
    flowers.append(Flower(start=int(dates[0]+dates[1]), end=int(dates[2]+dates[3]) ))

# 정렬이 핵심
flowers.sort()

def solution():
    start = 0
    
    for i in range(N):
        cur_flower = flowers[i]
        if cur_flower.end >= FIXED_END:
            start_idx = i
            start = cur_flower.start
            break

    if start == 0:
        return 0

    cnt = 1
    while start > FIXED_START and start_idx > 0:
        next_exists = False
        
        for i in range(start_idx):
            cur_flower = flowers[i]
            if cur_flower.end >= start:
                start_idx = i
                start = cur_flower.start
                cnt += 1
                next_exists = True
                break
        
        if not next_exists:
            return 0
    
    if start > FIXED_START:
        return 0
    else:
        return cnt

print(solution())

# 틀린 이유: 
# 예를 들어, 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미이다
# 문제 독해 똑바로 하자!!
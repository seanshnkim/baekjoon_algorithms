import sys
input = sys.stdin.readline
from collections import namedtuple
Flower = namedtuple("Flower", ["m1", "d1", "m2", "d2"])

N = int(input())
flowers = []

for _ in range(N):
    # 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 
    # 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미
    flowers.append(Flower(*map(int, input().split())))

# 정렬이 핵심
flowers.sort(key=lambda x: [x[0], x[1]])

def solution():
    start_month = 0
    start_day = 0
    
    for i in range(N):
        cur_flower = flowers[i]
        if cur_flower.m2 == 12:
            start_idx = i
            start_month = cur_flower.m1
            start_day = cur_flower.d1
            break

    if start_month == 0 and start_day == 0:
        return 0

    cnt = 1
    while start_month >= 3 and start_idx > 0:
        if start_month == 3 and start_day == 1:
            break
        
        next_exists = False
        
        for i in range(start_idx):
            cur_flower = flowers[i]
            if cur_flower.m2 > start_month or (cur_flower.m2 == start_month and cur_flower.d2 >= start_day):
                start_idx = i
                start_month = cur_flower.m1
                start_day = cur_flower.d1
                cnt += 1
                next_exists = True
                break
        
        if not next_exists:
            return 0
    
    if start_month > 3 or (start_month == 3 and start_day > 1):
        return 0
    else:
        return cnt

print(solution())

# 틀린 이유: 
# 예를 들어, 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미이다
# 문제 독해 똑바로 하자!!


'''
반례:
10
1 1 11 23
11 22 11 24
11 23 11 25
11 24 11 26
11 25 11 27
11 26 11 28
11 27 11 29
11 28 12 1
11 23 11 27
11 27 12 1
출력: 5
정답: 3

-> 이유: 피기 시작하는 날짜 - 마지막으로 핀 날짜 = 1 이어도 가능하기 때문이다.
나는 무조건 (피기 시작하는 날짜) - (마지막으로 핀 날짜) = 0 이어야 가능하다고 조건을 잡았다 -> 오류!
'''
import sys
input = sys.stdin.readline
from collections import namedtuple
Flower = namedtuple("Flower", ["start", "end"])

FIXED_START = 301
FIXED_END = 1130

N = int(input())
flowers = []

# 입력은 숫자가 아니라 문자열이다
def convert_date(month, day):
    
    m1 = ['5', '7', '10', '12']
    m2 = ['2', '4', '6', '8', '9', '11']
    
    if day == '1':
        if month in m1:
            month = str(int(month) - 1)
            day = '30'
        
        elif month in m2:
            month = str(int(month) - 1)
            day = '31'
        
        # month == 3인 경우
        elif month == '3':
            month = str(int(month) - 1)
            day = '28'
        
        # month == 1인 경우는 그냥 패스
            
    else:
        day = str(int(day) - 1)
    
    if len(day) == 1:
        day = '0' + day
        
    return int(month + day)



for _ in range(N):
    # dates = list(input().split())
    m1, d1, m2, d2 = input().split()
    
    # 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 
    # 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미
    # -> 지는 날짜가 입력으로 들어오므로, 처음부터 이걸 '피어있는 마지막 날짜'로 바꿔버리자.
    if len(d1) == 1:
        d1 = '0' + d1
    
    flowers.append(Flower(start=int(m1+d1), end=convert_date(m2, d2)) )

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
'''
import sys
input = sys.stdin.readline

# 빗물이 전혀 고이지 않는 경우도 고려

H, W = map(int, input().split())
heights = list(map(int, input().split()))

i = 0
while i < W and heights[i] == 0:
    i += 1
cur_max = heights[i]

j = i+1
cnt_moved = 0
acc_sum = 0
prev = cur_max

while j < W:
    cur = heights[j]
    if cur >= cur_max:
        cur_max = heights[j]
    
    elif cur < cur_max and cur > prev:
        acc_sum += cnt_moved * (cur - prev)
    
    prev = cur
    cnt_moved += 1
    j += 1

print(acc_sum)
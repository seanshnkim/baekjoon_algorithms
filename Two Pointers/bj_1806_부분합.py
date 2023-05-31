import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0, 0
cur_sum = 0
min_length = float('inf')

while True:
    if cur_sum >= S:
        min_length = min(min_length, right - left)
        cur_sum -= numbers[left]
        left += 1
        
    elif right == N:
        break
    
    else:
        cur_sum += numbers[right]
        right += 1


if min_length == float('inf'):
    print(0)
else:
    print(min_length)
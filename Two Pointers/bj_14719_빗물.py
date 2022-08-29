import sys

height_limit, width_limit = map(int, sys.stdin.readline().split())
height_list = list(map(int, sys.stdin.readline().split()))

def trap(heights) -> int:
    if not heights:
        return 0
    
    volume = 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]

    while left < right:
        left_max, right_max = max(heights[left], left_max), \
        max(heights[right], right_max)
        if left_max <= right_max:
            volume += left_max - heights[left]
            left += 1
        else:
            volume += right_max - heights[right]
            right -= 1

    return volume


print(trap(height_list))

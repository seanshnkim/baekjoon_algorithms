import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = max(nums) - min(nums)

while left <= right:
    mid = (left+right) // 2
    curr_max = curr_min = nums[0]
    cnt_interval = 1
    
    for n in nums:
        if n < curr_min:
            curr_min = n
        if n > curr_max:
            curr_max = n
        score = curr_max - curr_min
        
        # 구간을 현재 n부터 새로 시작
        if score > mid:
            cnt_interval += 1
            curr_min = curr_max = n
        if cnt_interval > M:
            break
    
    if cnt_interval > M:
        left = mid+1
    else:
        right = mid-1
    
print(left)
    
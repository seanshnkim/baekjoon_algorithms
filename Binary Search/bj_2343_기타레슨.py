import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# nums = 강의 길이
nums = list(map(int, input().split()))

left = 1
right = sum(nums)
mid = (left + right) // 2

while left <= right:
    mid = (left + right) // 2
    curr_sum = 0
    curr_cnt = 1
    
    
    #FIXME - 항상 순서대로 블루레이 CD에 담는게 아니다!!!
    for n in nums:
        curr_sum += n
        if curr_sum > mid:
            if n <= mid:
                curr_sum = n
                curr_cnt += 1
            else:
                left = mid+1
                break
        if curr_cnt > M:
            left = mid+1
            break
    if curr_cnt <= M:
        right = mid-1

print(left)

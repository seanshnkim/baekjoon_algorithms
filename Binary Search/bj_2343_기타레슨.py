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
    #FIXME - 만약 left = mid+1 이면 break하고, 이 if 문으로 가면 안된다.
    # 즉 n > mid일 때 여전히 curr_cnt <= M일 수도 있기 때문이다. 그러나 curr_cnt 값과 상관없이
    # left = mid+1하고 바로 while문에서 다시 시작해야 한다.
    # if curr_cnt <= M:
    if curr_cnt <= M and left != mid+1:
        right = mid-1

print(left)

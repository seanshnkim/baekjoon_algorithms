import sys

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

results = []
num_list.sort()

def solution(len_nums, nums):
    nums.sort()
    ans = nums[0], nums[1], nums[-1]
    min_sum = abs(sum(ans))

    for i in range(len_nums-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if abs(curr_sum) < min_sum:
                min_sum = abs(curr_sum)
                ans = nums[i], nums[left], nums[right]
            if curr_sum < 0:
                left += 1
            elif curr_sum > 0:
                right -= 1
            else:
                return ans
    return ans

print(*solution(N, num_list), sep=' ')

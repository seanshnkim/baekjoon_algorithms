import sys

len_num_list = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
target = int(input())

def brute_force_using_in(nums, targ):
    cnt = 0
    for i, n in enumerate(nums):
        comp = targ - n
        if comp in nums[i+1:]:
            cnt += 1

    return cnt

def using_dictionary(nums, targ):
    nums_map = {}
    cnt = 0

    for i, num in enumerate(nums):
        if (targ - num) in nums_map:
            cnt += 1
            # return [nums_map[target - num], i]
        nums_map[num] = i
    return cnt

# 하지만 이 문제는 인덱스를 구하는 문제가 아니라 단지 개수를 구하는 문제이기 때문에..!!
# nums should be sorted before
def using_two_pointers(nums, targ, len_nums):
    left, right = 0, len_nums - 1
    cnt = 0
    while not left == right:
        if nums[left] + nums[right] < targ:
            left += 1
        elif nums[left] + nums[right] > targ:
            right -= 1
        else:
            cnt += 1
            # right -= 1 이어도 상관없다.
            left += 1
    return cnt

num_list.sort()
print(using_two_pointers(num_list, target, len_num_list))
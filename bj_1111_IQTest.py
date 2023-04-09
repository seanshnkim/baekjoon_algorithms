import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

# 각 항이 모두 빠짐없이 일차방정식을 만족하는지 구한다.
# 이때 nums의 길이는 3 이상이라고 전제되어 있다.
def is_coherent(nums):
    # a, b 의 조합은 여러가지가 나올 수 있지만 다음 수는 항상 동일하다.
    # 4 4 1
    if nums[1] == nums[0]:
        if nums[2] != nums[1]:
            return 'B'
        else:
            for i in range(3, len(nums)):
                if nums[i] != nums[i-1]:
                    return 'B'
                
            return nums[-1]
    
    a = (nums[2] - nums[1]) / (nums[1] - nums[0])
    # if a == 0 이라면? 즉, nums[2] == nums[1]이라면?
    # => 불가능. 따라서 nums[1] == nums[0] 이면 nums[2] == nums[1]이다.
    
    if int(a) != a:
        return 'B'
    else:
        # a = 2.0
        a = int(a)
    
    # b는 항상 정수다.
    b = nums[1] - nums[0] * a
    
    for i in range(3, len(nums)):
        if nums[i] != nums[i-1]*a + b:
            return 'B'
        
    return nums[-1]*a + b


if N == 1:
    print('A')
elif N == 2:
    if numbers[0] == numbers[1]:
        print(numbers[1])
    else:
        print('A')
elif N >= 3:
    print(is_coherent(numbers))
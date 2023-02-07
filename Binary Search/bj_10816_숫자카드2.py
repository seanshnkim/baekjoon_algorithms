import sys
input = sys.stdin.readline


def upper_bound(arr, targ):
    # NOTE - ans 값은 꼭 초기화해주어야 한다.
    # 배열에 targ 값이 없다면 바로 ans 값을 리턴해야 하기 때문 -> 
    # local variable referenced before assignment 에러 발생한다.
    ans = 0
    left, right = 0, len(arr)-1
    
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == targ:
            ans = mid+1
            left = mid+1
        elif arr[mid] > targ:
            right = mid-1
        else:
            left = mid+1
    
    return ans


# lower bound
def lower_bound(arr, targ):
    # ans = 0
    left, right = 0, len(arr)-1
    
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == targ:
            ans = mid
            right = mid-1
        elif arr[mid] > targ:
            right = mid-1
        else:
            left = mid+1
        
    return ans


N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
targets = list(map(int, input().split()))

# 555 666 7 88
answers = []
for t in targets:
    answers.append(upper_bound(nums, t) - lower_bound(nums, t))

print(*answers)
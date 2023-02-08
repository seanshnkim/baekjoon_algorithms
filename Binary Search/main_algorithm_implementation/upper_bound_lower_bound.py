import sys
input = sys.stdin.readline

# upper bound: 현재 찾고자 하는 숫자보다 큰 수 중 첫번째(the first of greater numbers)
# lower bound: 현재 찾고자 하는 숫자보다 같거나 큰 수 중 첫번째(the first of greater or the same numbers)

# 상한, 하한은 binary search로 구현한다.

# upper bound
def upper_bound(arr, targ):
    left, right = 0, len(arr)-1
    ans = -1
    
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
    left, right = 0, len(arr)-1
    ans = -1
    
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == targ:
            #FIXME - 마지막에 left와 right가 같을 때, 
            # arr[left] == arr[right] == targ일 수도 있다
            # ans = mid-1
            ans = mid
            right = mid-1
        elif arr[mid] > targ:
            right = mid-1
        else:
            left = mid+1
    return ans
# 5 5 5 5 6 6 6 7 7 7
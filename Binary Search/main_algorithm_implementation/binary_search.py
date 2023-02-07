import sys
input = sys.stdin.readline

def binary_search(arr, targ):
    left, right = arr[0], arr[-1]
    position = -1
    
    #REVIEW 
    # 예시) targ position = 3, (l,r,m) = (3,5,4) -> (3,3,3)
    while left <= right:
        mid = (left+right) // 2
        
        if arr[mid] == targ:
            position = mid
            return position
        
        elif arr[mid] > targ:
            right = mid-1
        
        elif arr[mid] < targ:
            left = mid+1
    
    return position



input_arr = list(map(int, input.split()))
target = int(input())
search_arr = sorted(input_arr)
targ_pos = binary_search(search_arr, target)
# 주어진 input_arr에 target이 없다면 -1을 출력
print(targ_pos)




import sys
input = sys.stdin.readline

input_arr = list(map(int, input().split()))
# 5 10 13 19 6 21 24 41
def sort_(start, end):
    if start == end:
        return
    
    mid = (start+end) // 2
    sort_(start, mid)
    sort_(mid+1, end)
    merge(start, end)
    

def merge(start, end):
    b = [0]*(end-start+1)
    mid = (start+end) // 2
    i, j, k = start, mid+1, 0
    
    while i <= mid and j <= end:
        if input_arr[i] <= input_arr[j]:
            b[k] = input_arr[i]
            k += 1
            i += 1
        else:
            b[k] = input_arr[j]
            k += 1
            j += 1
    while i <= mid:
        b[k] = input_arr[i]
        k += 1
        i += 1
    while j <= end:
        b[k] = input_arr[j]
        k += 1
        j += 1
    
    for i in range(start, end+1):
        input_arr[i] = b[i-start]

sort_(0, len(input_arr)-1)
print(*input_arr)
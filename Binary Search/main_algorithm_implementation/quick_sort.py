import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))


def choose_pivot(low, high):
    return low + (high - low) // 2


def partition(low, high):
    pivot_idx = choose_pivot(low, high)
    pivot_val = arr[pivot_idx]
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    
    store_idx = low
    for i in range(low, high+1):
        if arr[i] < pivot_val:
            arr[i], arr[store_idx] = arr[store_idx], arr[i]
            store_idx += 1
    
    arr[store_idx], arr[high] = arr[high], arr[store_idx]
    return store_idx


def quick_sort(low, high):
    if low < high:
        pivot = partition(low, high)
        quick_sort(low, pivot-1)
        quick_sort(pivot+1, high)
    
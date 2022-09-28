import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start, end = 0, k
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(1, mid+1):
        cnt += min(mid//i, N)
    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
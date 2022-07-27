import sys

N, M = map(int, input().split())
lenList = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(lenList[-1] - M)
else:
    start = 0
    end = max(lenList)

    res = 0

    while(start <= end):
        total = 0
        mid = (start + end) // 2

        for l in lenList:
            if l > mid:
                total += l - mid
        
        # keep searching in lower segment (make mid smaller -> total gets larger)
        if total < M:
            end = mid - 1
        # mid can be a possible answer. Record into res variable, and keep searching in upper segment
        else:
            res = mid
            start = mid + 1

    print(res)
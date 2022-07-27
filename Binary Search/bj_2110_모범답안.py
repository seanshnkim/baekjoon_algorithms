import sys

N, C = map(int, input().split())

houseCd = []
for _ in range(N):
    houseCd.append(int(sys.stdin.readline()))

houseCd.sort()

# 통째로 외우자
def binary_search(array, start, end):
    ans = 0
    while start <= end:
        # mid is the distance
        mid = (start + end) // 2
        currCd = array[0]
        cnt = 1

        for i in range(1, N):
            if houseCd[i] >= currCd + mid:
                cnt += 1
                currCd = houseCd[i]

        # if the target is in upper(bigger) segment
        if cnt >= C:
            start = mid + 1
            ans = mid
        # if the target is in lower(smaller) segment
        else:
            end = mid - 1
    return ans

# minimum distance(start) = 1
start = 1
# maximum distance(end) = last coordinate - initial coordinate
end = houseCd[-1] - houseCd[0]

print(binary_search(houseCd, start, end))
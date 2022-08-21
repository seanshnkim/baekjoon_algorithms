import sys

N, C = map(int, input().split())

coordinates = []
for _ in range(N):
    coordinates.append(int(sys.stdin.readline()))

coordinates.sort()

# 통째로 외우자
def binary_search(cd_list, start, end):
    ans = 0
    while start <= end:
        # mid is the distance
        mid = (start + end) // 2
        curr_cd = cd_list[0]
        cnt = 1

        for i in range(1, N):
            if cd_list[i] >= curr_cd + mid:
                cnt += 1
                curr_cd = cd_list[i]

        # if the target is in upper(bigger) segment
        if cnt >= C:
            start = mid + 1
            ans = mid
        # if the target is in lower(smaller) segment
        else:
            end = mid - 1
    return ans

# minimum distance(start) = 1
min_dist = 1
# maximum distance(end) = last coordinate - initial coordinate
max_dist = coordinates[-1] - coordinates[0]

print(binary_search(coordinates, min_dist, max_dist))
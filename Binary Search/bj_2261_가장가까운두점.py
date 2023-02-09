import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
points = sorted(points, key=lambda x: x[0])


def solution(points, start, end):
    if (end - start) <= 2:
        if (end - start) == 1:
            return (points[end][0] - points[start][0])**2 + \
                    (points[end][1] - points[start][1])**2
        elif (end - start) == 2:
            # FIXME mid = (end - start) // 2 이런 바보같은 실수!
            mid = (end + start) // 2
            dist1 = (points[end][0] - points[mid][0])**2 + \
                    (points[end][1] - points[mid][1])**2
            dist2 = (points[mid][0] - points[start][0])**2 + \
                    (points[mid][1] - points[start][1])**2
            return min(dist1, dist2)
                
    mid = (start + end) // 2
    
    # squared distance
    #FIXME - d2 구할 때 mid+1부터 시작하면, points[mid]와 다른 점 사이 거리를 못 구한다.
    d1 = solution(points, start, mid)
    d2 = solution(points, mid, end)
    
    d = min(d1, d2)
    
    return merge_find(d, start, end)
    
    

def merge_find(dist, start, end):
    mid = (start+end) // 2
    
    ans = dist
    to_search = []
    i = 1
    # dist: squared distance
    while mid+i < len(points) and (points[mid+i][0] - points[mid][0])**2 <= dist:
        to_search.append(points[mid+i])
        i += 1
    i = 1
    while mid-i >= 0 and (points[mid][0] - points[mid-i][0])**2 <= dist:
        to_search.append(points[mid-i])
        i += 1
    
    # append points[mid] to to_search as well
    to_search.append(points[mid])
    # sort by y coordinate
    to_search = sorted(to_search, key=lambda x: x[1])
    
    for i in range(len(to_search)):
        for j in range(i+1, len(to_search)):
            if (to_search[j][1] - to_search[i][1])**2 > dist:
                break
            else:
                curr_dist = (to_search[j][0] - to_search[i][0])**2 + \
                            (to_search[j][1] - to_search[i][1])**2
                
                ans = min(curr_dist, ans)
    
    return ans


print(solution(points, 0, len(points)-1))
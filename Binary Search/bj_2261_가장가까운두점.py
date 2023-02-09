import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
points.sort()


def dist_sqrd(pA, pB):
    return (pA[0] - pB[0])*(pA[0] - pB[0]) + \
           (pA[1] - pB[1])*(pA[1] - pB[1])
        
        
def solution(points, start, end):
    if (end - start) == 1:
        return dist_sqrd(points[end], points[start])
    
    elif (end - start) == 2:
        # FIXME mid = (end - start) // 2 이런 실수 금지
        mid = (end + start) // 2
        d1_sqrd = dist_sqrd(points[end], points[mid])
        d2_sqrd = dist_sqrd(points[end], points[start])
        d3_sqrd = dist_sqrd(points[mid], points[start])
            
        return min(d1_sqrd, d2_sqrd, d3_sqrd)
                
    mid = (start + end) // 2
    
    # squared distance
    #FIXME - d2 구할 때 mid+1부터 시작하면, points[mid]와 다른 점 사이 거리를 못 구한다.?
    d1 = solution(points, start, mid)
    d2 = solution(points, mid+1, end)
    curr_dist = min(d1, d2)
    
    ans = curr_dist
    
    #REVIEW - points[mid]를 미리 넣어놔야 하나? YES
    to_search = [points[mid]]
    # dist: squared distance
    # FIXME - 범위가 0, 또는 len(points)가 아니라 start-1, end+1까지다
    # for i in range(mid+1, len(points)):
    for i in range(mid+1, end+1):
        x_diff = points[i][0] - points[mid][0]
        if x_diff*x_diff < ans:
            to_search.append(points[i])
            break
    for i in range(mid-1, start-1, -1):
        x_diff = points[mid][0] - points[i][0]
        if x_diff*x_diff < ans:
            to_search.append(points[i])
            break
        
    # sort by y coordinate
    to_search.sort(key=lambda x: (x[1], x[0]) )
    
    for i in range(len(to_search)-1):
        for j in range(i+1, len(to_search)):
            y_diff = to_search[j][1] - to_search[i][1]
            if y_diff*y_diff >= ans:
                break
            else:
                curr_dist_sqrd = dist_sqrd(to_search[j], to_search[i])
                ans = min(curr_dist_sqrd, ans)
    
    return ans


print(solution(points, 0, N-1))
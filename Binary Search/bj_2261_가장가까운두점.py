import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
points.sort(key=lambda x: x[0])


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
    #FIXME - d2 구할 때 mid+1부터 시작하면, points[mid]와 다른 점 사이 거리를 못 구한다.
    d1 = solution(points, start, mid)
    d2 = solution(points, mid, end)
    
    d = min(d1, d2)
    
    return merge_find(d, start, end)
    
    

def merge_find(dist, start, end):
    mid = (start+end) // 2
    ans = dist
    # append points[mid] to to_search as well
    to_search = [points[mid]]
    # dist: squared distance
    
    for i in range(mid+1, len(points)):
        x_diff = points[i][0] - points[mid][0]
        if x_diff*x_diff < ans:
            to_search.append(points[i])
            break
    for i in range(mid-1, -1, -1):
        x_diff = points[mid][0] - points[i][0]
        if x_diff*x_diff < ans:
            to_search.append(points[i])
            break
        
    # sort by y coordinate
    to_search.sort(key=lambda x: (x[1], x[0]) )
    
    for i in range(len(to_search)-1):
        for j in range(i+1, len(to_search)):
            y_diff = to_search[j][1] - to_search[i][1]
            if y_diff*y_diff >= dist:
                break
            else:
                curr_dist_sqrd = dist_sqrd(to_search[j], to_search[i])
                ans = min(curr_dist_sqrd, ans)
    
    return ans

print(solution(points, 0, len(points)-1))
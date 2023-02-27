from heapq import heappush, heappop

def solution(t, k, study, pstudy):
    
    visited = [0]*len(study)
    diff = [0]*k
    study_hq = [(s, i) for i, s in enumerate(study)]
    paper_hq = [(p, i) for i, p in enumerate(pstudy)]
    study_hq.sort()
    paper_hq.sort()
    sidx, pidx = 0, 0
    
    while sidx < len(study):
            
        if diff[0] + paper_hq[pidx][0] < study_hq[sidx][0]:
            c, i = paper_hq[pidx]
            c += diff[0]
            heappop(diff)
            heappush(diff, study[i] - pstudy[i])
        else:
            c, i = study_hq[sidx]
            
        if c > t:
            break
            
        t -= c
        visited[i] = 1
        
        while sidx < len(study) and visited[study_hq[sidx][1]]:
            sidx += 1
        while pidx < len(study) and visited[paper_hq[pidx][1]]:
            pidx += 1
        
    return sum(visited)

# study_list  = [10,11,12,50,93,94,95]
# pstudy_list = [2, 3, 4, 5, 6, 7, 8]
study_list  = [10, 11, 16, 22, 30]
pstudy_list = [ 2,  3, 14, 18, 20]
print(solution(60, 2, study_list, pstudy_list))
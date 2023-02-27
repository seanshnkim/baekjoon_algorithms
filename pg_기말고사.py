import heapq

# def solution(t, k, study, pstudy):
#     pstudy = [(s, i) for i, s in enumerate(pstudy)]
#     pstudy.sort()
#     study = [(s, i) for i, s in enumerate(study)]
#     study.sort()
    
#     acc_time = 0
#     answer = 0
#     selected = [False]*len(study)
#     while acc_time < t and answer < k:
#         s = heapq.heappop(pstudy)
#         acc_time += s[0]
#         selected[s[1]] = True
#         answer += 1
#     if acc_time > t:
#         return answer-1
#     elif acc_time == t:
#         return answer
#     else:
#         while acc_time < t:
#             s = heapq.heappop(study)
#             if not selected[s[1]]:
#                 acc_time += s[0]
#                 answer += 1
#         if acc_time > t:
#             return answer-1
#         else:
#             return answer


def solution(t, k, study, pstudy):
    pstudy_hq = [(time, i) for i, time in enumerate(pstudy)]
    pstudy_hq.sort()
    study_hq = [(time, i) for i, time in enumerate(study)]
    study_hq.sort()
    
    N = len(study)
    visited = [False]*N
    differences = []
    
    ps_idx = 0
    s_idx = 0
    acc_time = 0
    answer = 0
    
    while ps_idx < N and s_idx < N and acc_time < t:
        if k == 0:
            # (curr_diff, sel_idx)
            min_diff = heapq.heappop(differences)
            
            if pstudy_hq[ps_idx] < study_hq[s_idx]:
                sel_idx = pstudy_hq[ps_idx][1]
                if not visited[sel_idx]:
                    curr_diff = study[sel_idx][0]-pstudy[sel_idx][0]
                    if curr_diff > min_diff[0]:
                        visited[min_diff[1]] = False
                        visited[sel_idx] = True
                        # NOTE - 포기!!!
        
        if pstudy_hq[ps_idx] < study_hq[s_idx]:
            sel_idx = pstudy_hq[ps_idx][1]
            if not visited[sel_idx]:
                # (time, i)
                visited[sel_idx] = True
                k -= 1
                curr_diff = study[sel_idx][0]-pstudy[sel_idx][0]
                heapq.heappush(differences, (curr_diff, sel_idx) )
                acc_time += pstudy[sel_idx][0]
                answer += 1
                
            ps_idx += 1
            
        else:
            sel_idx = study_hq[s_idx][1]
            if not visited[sel_idx]:
                # (time, i)
                visited[sel_idx] = True
                k -= 1
                curr_diff = study[sel_idx][0]-pstudy[sel_idx][0]
                heapq.heappush(differences, (curr_diff, sel_idx) )
                acc_time += study[sel_idx][0]
                answer += 1
                
            s_idx += 1
    
    if acc_time >= t:
        if acc_time > t:
            return answer-1
        else:
            return answer
    if k == 0:
        min_diff = heapq.heappop(differences)
        
        

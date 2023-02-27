import heapq

def solution(t, k, study, pstudy):
    pstudy = [(s, i) for i, s in enumerate(pstudy)]
    pstudy.sort()
    study = [(s, i) for i, s in enumerate(study)]
    study.sort()
    
    acc_time = 0
    answer = 0
    selected = [False]*len(study)
    while acc_time < t and answer < k:
        s = heapq.heappop(pstudy)
        acc_time += s[0]
        selected[s[1]] = True
        answer += 1
    if acc_time > t:
        return answer-1
    elif acc_time == t:
        return answer
    else:
        while acc_time < t:
            s = heapq.heappop(study)
            if not selected[s[1]]:
                acc_time += s[0]
                answer += 1
        if acc_time > t:
            return answer-1
        else:
            return answer
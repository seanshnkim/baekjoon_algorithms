import sys

nTestCase = int(input())

for t in range(nTestCase):
    nApplic = int(input())
    resume_interv = {}
    interv_resume = {}
    cntRecruit = nApplic

    for n in range(nApplic):
        resume, interview = map(int, sys.stdin.readline().split())
        resume_interv[resume] = interview
        interv_resume[interview] = resume
    
    # 서류 심사(resume) 기준으로 꼴지부터 차례로 (순위 기준 내림차순으로) 정렬
    resume_sorted = sorted(resume_interv.items(), reverse=True)

    for resumeMy, intervMy in resume_sorted:
        if resumeMy == 1:
            break
        # 만약 서류, 면접 둘다 꼴찌라면 비교할 필요도 없이 탈락
        if resumeMy == nApplic and intervMy == nApplic:
            cntRecruit -=1
            continue
        intervRank = intervMy
        while intervRank > 1:
            intervRank -= 1
            # 나보다 면접 성적이 좋은(순위가 높은) 녀석의 서류 성적(resume rank)도 나보다 순위가 높다면(rank 숫자가 작다면)
            # 나는 탈락 -> 최종 신입사원 수에서 1 차감
            rivalResumeRank = interv_resume[intervRank]
            if rivalResumeRank < resumeMy:
                cntRecruit -= 1
                break

    print(cntRecruit)


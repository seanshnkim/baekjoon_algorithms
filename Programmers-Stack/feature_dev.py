def solution(progresses, speeds):
    dayDeploy = []
    # progresses에 원소가 남아있을 때까지
    while progresses:
        numDeploy = 0
        # progress의 각 원소에 speeds를 더해
        progresses = [sum(x) for x in zip(progresses, speeds)]
        print("How many elements:", len(progresses))

        # 맨 앞 원소가 100이면 계속 맨 앞 원소를 제거한다.
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            numDeploy += 1
        dayDeploy.append(numDeploy)

    return dayDeploy

########################################################################################################

def solution2(progresses, speeds):
    dayDeploy = []

    # progresses에 원소가 남아있을 때까지
    while progresses:
        numDeploy = 0
        # progress의 각 원소에 speeds를 더해
        progresses = [sum(x) for x in zip(progresses, speeds)]

        while progresses:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                numDeploy += 1

    #                 print(len(progresses))
    return dayDeploy

########################################################################################################

def solution3(progresses, speeds):
    dayDeploy = []

    # progresses에 원소가 남아있을 때까지
    while progresses:
        numDeploy = 0
        # progress의 각 원소에 speeds를 더해
        progresses = [sum(x) for x in zip(progresses, speeds)]

        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            numDeploy += 1
            if not progresses:
                dayDeploy.append(numDeploy)
                break
        dayDeploy.append(numDeploy)

########################################################################################################

def solution4(progresses, speeds):
    dayDeploy = []

    # progresses에 원소가 남아있을 때까지
    while progresses:
        numDeploy = 0
        # progress의 각 원소에 speeds를 더해
        progresses = [sum(x) for x in zip(progresses, speeds)]

        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            numDeploy += 1
            if not progresses:
                dayDeploy.append(numDeploy)
                break
        if numDeploy != 0:
            dayDeploy.append(numDeploy)

    return dayDeploy

########################################################################################################
def solution5(progresses, speeds):
    dayDeploy = []
    deployList = []

    # progresses에 원소가 남아있을 때까지
    while progresses:

        # progress의 각 원소에 speeds를 더해
        progresses = [sum(x) for x in zip(progresses, speeds)]

        while progresses[0] >= 100:
            deployList.append(progresses.pop(0))
            speeds.pop(0)
            if not progreses:
                break
    return dayDeploy
########################################################################################################
def solution_best(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
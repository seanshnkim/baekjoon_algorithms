from collections import deque

def solution(tickets):
    visited = [False] * len(tickets)
    toVisit = deque()
    route = ["ICN"]

    temp = []
    for t in range(len(tickets)):
        start, destination = tickets[t][0], tickets[t][1]
        if start == "ICN":
            temp.append(destination)
    # 방문해야 할 문자열(공항)이 여러 개이면, 알파벳 순으로 정렬한 다음 가장 첫번째 문자열을 destination에 넣는다.
    destination = sorted(temp)[0]
    toVisit.append(destination)

    while toVisit:
        for currAirport in toVisit:
            for t in range(len(tickets)):
                start, destination = tickets[t][0], tickets[t][1]
                if visited[t] == False and start == currAirport:
                    toVisit.append(destination)
                    visited[t] = True

    answer = []
    return answer

def solution2(tickets):
    start = 'ICN'
    ticketStack = tickets
    answerRoute = [start]

    print(ticketStack)

    while ticketStack:
        for t in range(len(ticketStack)):
            print(ticketStack, t)
            if ticketStack[t][0] == start:
                print(start)
                start = ticketStack[t][1]
                print(start)
                answerRoute.append(start)
                print(ticketStack, f'answerRoute: {answerRoute}')
                ticketStack.pop(t)

    return f'This is answeRoute: {answerRoute}'

def solution_naive(tickets):
    start = 'ICN'
    answerRoute = [start]
    visited = [False] * len(tickets)

    while any(v == False for v in visited):
        for t in range(len(tickets)):
            if tickets[t][0] == start and visited[t] == False:
                start = tickets[t][1]
                answerRoute.append(start)
                visited[t] = True
                print(tickets[t])
                break
    return answerRoute

def solution_v1(tickets):
    start = 'ICN'
    answerRoute = [start]
    visited = [False] * len(tickets)
    unsortedList = []

    # while any(v == False for v in visited):
    # while문이 멈추지 않아서 디버깅을 위해 우선 8번만 돌려보기로 하자.
    for i in range(8):
        print(visited)
        for t in range(len(tickets)):
            if tickets[t][0] == start and visited[t] == False:
                # tickets[1]이 아니라 tickets[t][1]. 어처구니없는 실수지만 30분을 헤맸다...
                unsortedList.append((tickets[1], t))
        start = sorted(unsortedList)[0]
        print('unsortedList: ', unsortedList)
        print('start[0]: ', start[0])
        answerRoute.append(start[0][1])
        visited[start[1]] = True
        print(tickets[start[1]])
        print('start: ', start[0])

    return answerRoute

def solution_v2(tickets):
    start = 'ICN'
    answerRoute = [start]
    visited = [False] * len(tickets)

    while any(v == False for v in visited):
    #for i in range(3):
        print(f'\nvisited: {visited}')
        # 아... unsortedList 매 loop마다 초기화해주는 거 깜빡했다
        unsortedList = []
        for t in range(len(tickets)):
            if tickets[t][0] == start and visited[t] == False:
                unsortedList.append((tickets[t][1], t))
                print('unsortedList should have city that starts from "start"')
                print(f'This is tickets:{tickets}')
                print(f'unsortedList:{unsortedList}')
        # 예시) start = ('HAL', 3)
        print("start should be the first in alphabetical order")

        # 버그 발견: start의 자료형이 통일이 안돼서!!!
        # for loop 안에는 start를 그냥 문자열로 설정했는데 아래에선 start를 (문자열, 숫자) 튜플 형태로 저장했으니까...
        start = sorted(unsortedList)[0][0]
        currInd = sorted(unsortedList)[0][1]
        # start[0] = 'HAL'
        print('start should be just string type: ', start)
        answerRoute.append(start)
        print(f'answerRoute: {answerRoute}')
        visited[currInd] = True
        #print(f'After {i}th iteration, visited should have onlt True values: {visited}')

    return answerRoute

def solution_v3(tickets):
    start = 'ICN'
    answerRoute = [start]
    visited = [False] * len(tickets)

    while any(v == False for v in visited):
        startCandidates = []

        for t in range(len(tickets)):
            # 모든 티켓을 다 돌면서 각 ticket이 1)아직 방문하지 않았고 2)현재 출발지인 start가 있다면
            if tickets[t][0] == start and visited[t] == False:
                # 우선 출발지를 포함하는 티켓이 있다면, 그 티켓을 임시로 저장한다.
                startCandidates.append((tickets[t][1], t))
                # 출발지를 포함하는 티켓이 여러 개가 나올 수 있기 때문에 알파벳 순으로 정렬해서, 가장 먼저 나오는 녀석을 선택해야 한다.
                startSorted = deque(sorted(startCandidates))
                start, currInd = startSorted.popleft()
                # 그런데 또 고른 새로운 출발지가 유효하지 않을 수 있다.
                # start가 유효하다는 것은 start를 출발지로 하는 티켓이 정말 있는지 여부다.
                startValid = False

                # start가 유효하지 않다면 계속 확인해야 한다. 그리고 startSorted에도 후보군이 남아있을 때까지.
                while not startValid and startSorted:
                    # tickets을 하나씩 다 돌면서
                    for t_again in range(len(tickets)):
                        # 근데 이렇게 하는 것보다 스택을 만들어서 점점 원소 개수 줄여나가면서 그 스택 안에서 돌게 하는 게 효율적이지 않을까?

                        # 다 돌았는데도 없다면 start를 다른 후보로 교체, 그리고 다른 후보에 대해서도 동일한 과정 반복

                        # start를 출발점으로 하는 티켓이 있는지 확인.
                        if tickets[t_again][0] == start:
                            # 있다면 전체 while loop를 중단해야
                            startValid = True
                            break
                        else:
                            startValid = False
                    if startValid == False:
                        start, currInd = startSorted.popleft()

        answerRoute.append(start)
        print(f'answerRoute: {answerRoute}')
        visited[currInd] = True

    return answerRoute


testTickets_naive = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
testTickets_complicate = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
testTickets_2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

# ICN > ATL > ICN > SFO > ATL > SFO

#print(solution_naive(testTickets_naive))
#print(solution_v2(testTickets_naive))
print(solution_v3(testTickets_2))
#print(solution_final(testTickets_complicate))







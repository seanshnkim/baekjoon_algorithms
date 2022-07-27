def solution(priorities, location):
    indexList = []

    for i in range(len(priorities)):
        indexList.append(i)

    count = 0

    while (priorities[0] != max(priorities)) | (indexList[0] != location):
        while priorities[0] == max(priorities):
            if indexList[0] == location:
                count += 1
                return count
            else:
                priorities.pop(0)
                indexList.pop(0)
                count += 1

        priorities.append(priorities.pop(0))
        indexList.append(indexList.pop(0))
    return count+1

################################################################################################################
def solution2(priorities, location):
    queuePrinter = [(i,p) for i,p in enumerate(priorities)]
    count = 0

    head= queuePrinter.pop(0)
    # 버그 : priorities는 pop을 하지 않기 때문에 max값이 업데이트되지 않고, 초기 max값으로 유지된다. 그래서 while loop이 끝나지 않고 계속 돈다.
    while (head[1] != max(priorities)) | (head[0] != location):
        if head[0] != location:
            count += 1
        else:
            queuePrinter.append(head)
            count += 1

    return count + 1

################################################################################################################
def solution2(priorities, location):
    queuePrinter = [(i,p) for i,p in enumerate(priorities)]
    count = 0

    head= queuePrinter.pop(0)
    # 버그 : priorities는 pop을 하지 않기 때문에 max값이 업데이트되지 않고, 초기 max값으로 유지된다. 그래서 while loop이 끝나지 않고 계속 돈다.
    while any(head[1] < q[1] for q in queuePrinter) | (head[0] != location):
        if head[0] != location:
            count += 1
        else:
            queuePrinter.append(head)
            count += 1

    return count + 1

################################################################################################################

def solution_best(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
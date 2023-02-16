from collections import Counter
def solution(participant, completion):
    answer = ''
    #두 집합의 차집합을 구하기
    collection = Counter(participant) - Counter(completion)
    for i in collection:
        answer = i
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
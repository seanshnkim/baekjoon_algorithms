'''2022-02-25
출처 : 프로그래머스 > 코딩테스트 고득점 kit > 해시 > 완주하지 못한 선수
'''

# def solution(participant, completion):
#     for p in participant:
#         if p in completion:
#             completion.remove(p)
#             participant.remove(p)
#             print('completion:', completion)
#             print('participant:', participant)
#     return participant


def sol2(participant, completion):
    for c in completion:
        if c in participant:
            participant.remove(c)
    return participant[-1]

''' https://velog.io/@matisse/완주하지-못한-선수-python '''
# count 함수를 이용
def solution2(participant, completion):
    for p in participant:
        if participant.count(p) > completion.count(p):
                return p

# set을 이용
# 결점 : participant, 또는 completion에는 동명이인이 있을 수 있다.
def solution3(participant, completion):
    player = list(set(participant)-set(completion))
    if player:
        return player[0]

# zip 함수를 이용
def solution4(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

# 파이썬의 collections.Counter를 이용
import collections

def solution5(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 딕셔너리를 이용, 해쉬 함수
def solution6(participant, completion):
    hashTable = {}
    val = 0
    for p in participant:
        hashTable[hash(p)] = p
        val += hash(p)
    for c in completion:
        val -= hash(c)
    return hashTable[val]

par = ["leo", "kiki", "eden"]
comp = ["eden", "kiki"]

# print(solution(par, comp))
print(sol2(par, comp))


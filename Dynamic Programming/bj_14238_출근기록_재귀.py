import sys
from itertools import permutations
input = sys.stdin.readline

records = input().rstrip('\n')
'''
CABAC라고 하자
CABA, C -> okay
    -> CAB, A -> okay
        -> CA, B -> okay
            -> C, A -> okay
                -> C -> okay
'''

def dfs(seq, idx):
    # 현재 문자열의 길이가 0이라면
    if idx == 0:
        return idx
        
    if seq[idx] == 'A':
        return dfs(seq, idx-1)
    elif seq[idx] == 'B':
        if seq[idx-1] != 'B':
            return dfs(seq, idx-1)
        else:
            return -1
    else:
        if idx > 1:
            if seq[idx-1] != 'C' and seq[idx-2] != 'C':
                return dfs(seq, idx-1)
            else:
                return -1
        elif idx == 1:
            if seq[0] != 'C':
                return 0
            else:
                return -1


def solution(records):
    len_rec = len(records)
    
    for sequence in permutations(records):
        sequence = ''.join(sequence)
        res = dfs(sequence, len_rec-1)
        if res != -1:
            return sequence
    return -1

print(solution(records))
    
'''
S의 모든 순열 중에서 올바른 출근 기록인 것을 하나만 출력한다.
만약, 올바른 출근 기록이 없는 경우에는 -1을 출력한다.

AAA...
B*B*B...
C**C**C...
'''
import sys
from itertools import permutations
input = sys.stdin.readline

records = input().rstrip('\n')
L = len(records)

# L <= 50 -> 최대 크기: 125000
# -1 : 업데이트 X
dp = [ [[-1]*(L+1) for _ in range(L+1)] for _ in range(L+1)]
'''
CABAC라고 하자
CABA, C -> okay
    -> CAB, A -> okay
        -> CA, B -> okay
            -> C, A -> okay
                -> C -> okay
'''

def dfs(seq, numA, numB, numC, idx):
    # 현재 문자열의 길이가 0이라면
    if idx == 0:
        return idx
    
    # 만약 현재 리턴하려는 값 dp[numA][numB][numC]이 -2이거나 -1이라면, 
    # 0 이상이 될 때까지 업데이트를 해보아야 한다. 그게 아니면, 바로 dp 값을 출력한다.
    if dp[numA][numB][numC] >= 0:
        return dp[numA][numB][numC]
        
    if seq[idx] == 'A':
        if dp[numA-1][numB][numC] == -1:
            dp[numA-1][numB][numC] = dfs(seq, numA-1, numB, numC, idx-1)
        
        dp[numA][numB][numC] = dp[numA-1][numB][numC]
    
    elif seq[idx] == 'B':
        if seq[idx-1] != 'B':
            if dp[numA][numB-1][numC] == -1:
                dp[numA][numB-1][numC] = dfs(seq, numA, numB-1, numC, idx-1)
            dp[numA][numB][numC] = dp[numA][numB-1][numC]

    else:
        if idx > 1:
            if seq[idx-1] != 'C' and seq[idx-2] != 'C':
                if dp[numA][numB][numC-1] == -1:
                    dp[numA][numB][numC-1] = dfs(seq, numA, numB, numC-1, idx-1)
        elif idx == 1:
            if seq[0] != 'C':
                if dp[numA][numB][numC-1] == -1:
                    dp[numA][numB][numC-1] = 0
        dp[numA][numB][numC] = dp[numA][numB][numC-1]
        
    return dp[numA][numB][numC]


def solution(records):
    len_rec = len(records)
    nA = records.count('A')
    nB = records.count('B')
    nC = len_rec - (nA+nB)
    
    set_perm = set()
    for sequence in permutations(records):
        sequence = ''.join(sequence)
        if sequence not in set_perm:
            res = dfs(sequence, nA, nB, nC, len_rec-1)
            set_perm.add(sequence)
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
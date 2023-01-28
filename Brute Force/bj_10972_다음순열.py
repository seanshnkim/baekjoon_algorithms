import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

def solution():
    idx = N-1
    while idx > 0 and seq[idx-1] > seq[idx]:
        idx -= 1

    if idx == 0:
        return -1
    # swap
    # seq[idx-1], seq[idx] = seq[idx], seq[idx-1]
    # seq[idx:] = seq[idx:][::-1]
    '''
    반례: 4
         2 4 3 1
    정답: 3 1 2 4
    결과: 4 1
    '''
    # 1. if seq[idx-1] == 4, then swap seq[idx-1] with 4+1
    # 2. Find the index of 4+1 = 5, next_idx
    # 3. swap seq[next_idx] with 4 (== seq[idx-1])
    next_val = seq[idx-1] + 1
    next_idx = seq.index(next_val)
    seq[idx-1], seq[next_idx] = next_val, seq[idx-1]
    seq[idx:] = sorted(seq[idx:])
    
    return ' '.join(map(str, seq))


print(solution())
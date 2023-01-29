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
    결과: 4 1 3 2
    '''
    # 1. if seq[idx-1] == 4, then swap seq[idx-1] with 4+1
    # 2. Find the index of 4+1 = 5, next_idx
    # 3. swap seq[next_idx] with 4 (== seq[idx-1])
    #FIXME - WRONG!! 
    '''
    next_val = seq[idx-1] + 1
    next_idx = seq.index(next_val)
    seq[idx-1], seq[next_idx] = next_val, seq[idx-1]
    seq[idx:] = sorted(seq[idx:])
    반례: 4
        2 1 4 3
    정답: 2 3 1 4
    결과: 1 2 3 4
    '''
    # Find the one greater than seq[idx-1] but the smallest among seq[idx:]
    target_idx = idx-1
    smallest = N+1
    for i in range(idx, N):
        if seq[i] > seq[idx-1] and seq[i] < smallest:
            smallest = seq[i]
            target_idx = i
    
    seq[idx-1], seq[target_idx] = seq[target_idx], seq[idx-1]
    seq[idx:] = sorted(seq[idx:])
    
    return ' '.join(map(str, seq))


print(solution())
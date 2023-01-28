import sys

N = int(sys.stdin.readline())
seq = list(sys.stdin.readline().split())

def solution():
    idx = N-1
    while idx > 0 and seq[idx-1] > seq[idx]:
        idx -= 1

    if idx == 0:
        return -1
    # swap
    seq[idx-1], seq[idx] = seq[idx], seq[idx-1]
    # seq[idx+1:] -> change from descending order to ascending order
    seq[idx:] = seq[idx:][::-1]
    
    return ' '.join(seq)


print(solution())
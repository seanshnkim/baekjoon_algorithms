import sys
input = sys.stdin.readline

pattern = "ABCABE"
N = len(pattern)
fail = [0]*N

def match_idx(curr_char, curr_idx):
    if curr_idx == 0:
        return 0
    
    moved_idx = fail[curr_idx-1]
    if curr_char == pattern[moved_idx]:
        return moved_idx+1
    else:
        return match_idx(curr_char, moved_idx)


def complete_fail_array(input_str):
    for i in range(1, N):
        curr_char = input_str[i]
        fail[i] = match_idx(curr_char, i)

complete_fail_array(pattern)


def search_string(given_str, pattern):
    cnt = 0
    start = 0
    N = len(pattern)
    
    while cnt < N and start <= len(given_str)-N+1:
        for i in range(N):
            if given_str[start+i] != pattern[i]:
                start = (start + i) - fail[i-1]
                cnt = 0
                break
            else:
                cnt += 1
    if cnt < N:
        return -1
    else:
        return start
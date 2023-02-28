import sys
input = sys.stdin.readline

given_str = input().rstrip('\n')
pattern = input().rstrip('\n')

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


def complete_fail_array():
    for i in range(1, N):
        curr_char = pattern[i]
        fail[i] = match_idx(curr_char, i)


def search_string():
    start = 0
    answer = 0
    locations = []
    
    # while start <= len(given_str)-N+1:
    while start <= len(given_str) - N:
        cnt = 0
        
        
        # FIXME - 무한 루프
        # for i in range(N):
        for i in range(N):
            if given_str[start+i] != pattern[i]:
                if i == 0:
                    start += 1
                else:
                    start = (start + i) - fail[i-1]
                cnt = 0
                break
            else:
                cnt += 1
        if cnt == N:
            answer += 1
            # 문제에서는 idx=0에서의 문자를 1번째라고 간주
            locations.append(start+1)
            start += N
        
    return answer, locations


complete_fail_array()
answer, locations = search_string()
print(answer)
print(*locations)
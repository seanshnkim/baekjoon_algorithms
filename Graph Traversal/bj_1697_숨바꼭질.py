import sys
from collections import deque

MAX_N = 100001
depths = [-1]*MAX_N
curr, targ = map(int, sys.stdin.readline().split())
q = deque()

def bfs(q):
    while q:
        curr_loc = q.popleft()
        curr_depth = depths[curr_loc]
        
        next_locs = [curr_loc-1, curr_loc+1, curr_loc*2]
        for next in next_locs:
            # FIXME - if 0 <= next and next <= MAX_N:
            # 범위 실수, 사소한 실수 고치자
            if 0 <= next and next < MAX_N:
                if next == targ:
                    return curr_depth+1
                if depths[next] == -1:
                    depths[next] = curr_depth+1
                    q.append(next)
    
    return curr_depth
        

if curr == targ:
    print(0)
else:
    depths[curr] = 0
    q.append(curr)
    print(bfs(q))
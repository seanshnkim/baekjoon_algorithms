import sys
from collections import deque

MAX_N = 100001
depths = [-1]*MAX_N
curr, targ = map(int, sys.stdin.readline().split())
q = deque()


def bfs(q):
    cnt = 0
    min_depth = 0
    while q:
        curr_loc = q.popleft()
        curr_depth = depths[curr_loc]
        
        next_locs = [curr_loc-1, curr_loc+1, curr_loc*2]
        for next in next_locs:
            if 0 <= next and next < MAX_N:
                if next == targ:
                    if min_depth == 0:
                        min_depth = curr_depth+1
                        cnt += 1
                    else:
                        # 반복문을 통해 경유하는 loc들의 모임은 항상 다른가?
                        if curr_depth+1 == min_depth:
                            cnt += 1
                    
                if depths[next] == -1:
                    depths[next] = curr_depth+1
                    q.append(next)
    
    return min_depth, cnt
        

if curr == targ:
    print(0)
else:
    depths[curr] = 0
    q.append(curr)
    time, num_ways = bfs(q)
    print(time)
    print(num_ways)
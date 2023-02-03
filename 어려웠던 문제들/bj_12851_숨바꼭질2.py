import sys
from collections import deque

MAX_N = 100000
depths = [[-1]*3 for _ in range(MAX_N+1)]
curr, targ = map(int, sys.stdin.readline().split())
q = deque()


def bfs(q):
    cnt = 0
    min_depth = 0
    
    while q:
        curr_loc = q.popleft()
        
        next_locs = [curr_loc-1, curr_loc+1, curr_loc*2]
        for i in range(3):
            if 0 <= next_locs[i] and next_locs[i] < MAX_N+1:
                if next_locs[i] == targ:
                    if min_depth == 0:
                        min_depth = depths[curr_loc][i]+1
                        cnt += 1
                    else:
                        # 반복문을 통해 경유하는 loc들의 모임은 항상 다른가?
                        if depths[curr_loc][i]+1 == min_depth:
                            cnt += 1
                
                # 이제는 기존에 방문했던 노드도 다시 한번 확인해야 하므로 이 if문은 안된다.
                # if depths[next] == -1:
                if depths[next_locs[i]][i] == -1:
                    depths[next_locs[i]][i] = depths[curr_loc][i]+1
                    q.append(next_locs[i])
    
    return min_depth, cnt
        

if curr == targ:
    print(0)
    print(1)
else:
    # depths[curr] = 0
    depths[curr] = [0, 0, 0]
    q.append(curr)
    time, num_ways = bfs(q)
    print(time)
    print(num_ways)
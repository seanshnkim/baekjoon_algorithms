import sys
from collections import deque

MAX_N = 1000001
depths = [-1]*(MAX_N)
curr, targ = map(int, sys.stdin.readline().split())
q = deque()


def bfs(q):
    cnt = 0
    min_depth = 0
    
    while q:
        curr_loc = q.popleft()
        curr_depth = depths[curr_loc]
        
        #REVIEW - 이 한 줄 추가로 굉장한 시간 단축을 노릴 수 있다?
        if min_depth != 0 and curr_depth > min_depth:
            continue
        
        next_locs = [curr_loc-1, curr_loc+1, curr_loc*2]
        for next in next_locs:
            if 0 <= next and next < MAX_N:
                if next == targ:
                    if depths[targ] == -1:
                        min_depth = curr_depth+1
                    if curr_depth+1 == min_depth:
                        cnt += 1
                    # if next == targ이면 그 뒤에 아무것도 안해도 되나?
                # 이제는 기존에 방문했던 노드도 다시 한번 확인해야 하므로 이 if문은 안된다.
                # if depths[next] == -1:
                if depths[next] == -1 or curr_depth+1 <= depths[next]:
                    depths[next] = curr_depth+1
                    q.append(next)
    
    return min_depth, cnt
        

if curr == targ:
    print(0)
    print(1)
else:
    depths[curr] = 0
    q.append(curr)
    time, num_ways = bfs(q)
    print(time)
    print(num_ways)
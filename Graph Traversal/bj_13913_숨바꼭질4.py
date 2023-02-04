import sys
from collections import deque
sys.setrecursionlimit(1000000)

MAX_N = 100001
curr, targ = map(int, sys.stdin.readline().split())

visited = [-1]*MAX_N
came_from = [-1]*MAX_N

visited[curr] = 0
came_from[curr] = curr
 

def bfs(q):
    while q:
        curr_loc = q.popleft()
        curr_depth = visited[curr_loc]
        next_locs = [curr_loc-1, curr_loc+1, curr_loc*2]
        
        for next in next_locs:
            if 0 <= next < MAX_N:
                if visited[next] == -1:
                    visited[next] = curr_depth+1
                    came_from[next] = curr_loc
                    q.append(next)
                    
                    if next == targ:
                        return visited[next]
                    
    return curr_depth


def print_came_from(end, start):
    orig_end = end
    if end != start:
        end = start
        start = came_from[start]
        print_came_from(end, start)
        
    print(orig_end, end=' ')
    return

# 이 if문은 꼭 필요하다. 만약 도착점(targ)이 시작점(curr)과 같다면, 
# 시작점의 next는 curr과 항상 다르기 때문에(+1, -1, 또는 2배의 값) 포함되지 않기 때문이다.
if curr == targ:
    print(0)
    print(curr)
else:
    q = deque([curr])
    print(bfs(q))
    print_came_from(targ, came_from[targ])
    
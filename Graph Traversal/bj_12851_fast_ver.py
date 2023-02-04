import sys
from collections import deque

MAX_N = 100001
curr, targ = map(int, sys.stdin.readline().split())
# [cnt, num_ways]
visited = [[-1, 0] for _ in range(MAX_N)]
visited[curr] = [0, 1]


def bfs(q):
    while q:
        curr_loc = q.popleft()
        next_locs = [curr_loc-1, curr_loc+1, curr_loc*2]
        
        for next in next_locs:
            if 0 <= next < MAX_N:
                if visited[next][0] == -1:
                    visited[next][0] = visited[curr_loc][0] + 1
                    visited[next][1] = visited[curr_loc][1]
                    q.append(next)
                    
                elif visited[next][0] == visited[curr_loc][0] + 1:
                    visited[next][1] += visited[curr_loc][1]

q = deque()
q.append(curr)
bfs(q)
print(visited[targ][0])
print(visited[targ][1])
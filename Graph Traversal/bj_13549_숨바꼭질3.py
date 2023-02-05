import sys
from collections import deque

MAX_N = 200000 
dist = [-1]*MAX_N

start, dest = map(int,input().split())

dist[start] = 0
q = deque([start])

# BFS는 DFS처럼 재귀함수를 쓰는 게 아니라서 따로 함수로 만들 필요가 없었다.
while q:
    curr = q.popleft()
    next_steps = [curr*2, curr-1, curr+1]
    for next in next_steps:
        if 0 <= next < MAX_N and dist[next] == -1:
            # 가중치가 0인 경우, 1) deque의 앞에 삽입   2) dist 값을 그대로 유지
            if next == curr*2:
                q.appendleft(next)
                dist[next] = dist[curr]
            # 가중치가 1이면 1) deque의 뒤에 삽입   2) dist 값을 1 증가시킨 후 대입
            else:
                q.append(next)
                dist[next] = dist[curr]+1

print(dist[dest])
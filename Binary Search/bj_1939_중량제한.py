import sys
from collections import deque

input = sys.stdin.readline

V, E = map(int, input().split())
adj_list = [[]*(V+1) for _ in range(V+1)]

w_max = 1
w_min = 1000000000
for _ in range(E):
    v1, v2, w = map(int, input().split())
    adj_list[v1].append((v2, w))
    adj_list[v2].append((v1, w))
    if w > w_max:
        w_max = w
    if w < w_min:
        w_min = w

start, dest = map(int, input().split())
visited = [False]*(V+1)

def solution(visited, left, right):
    while left <= right:
        mid = (left + right) // 2
        
        q = deque([start])
        while q:
            curr = q.popleft()
            
            for adj_v in adj_list[curr]:
                if (not visited[adj_v[0]]) and mid <= adj_v[1]:
                    visited[adj_v[0]] == True
                    q.append(adj_v)

                    if adj_v == dest:
                        
                        visited = [False]*(V+1)
                        return solution(visited, mid+1, right)
        right = mid-1
        
    return mid


print(solution(visited, w_min, w_max))
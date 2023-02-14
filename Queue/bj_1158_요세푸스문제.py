import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

q = deque([i for i in range(1, N+1)] )

answer = []
while q:
    for i in range(K-1):
        q.append(q.popleft())
    answer.append(q.popleft())

print('<', ', '.join(map(str, answer) ), '>', sep='')
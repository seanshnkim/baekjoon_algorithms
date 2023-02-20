import sys
input = sys.stdin.readline
import heapq
from sys import maxsize

V = int(input())
E = int(input())

adj_list = [[] for _ in range(V + 1)]
visited = [maxsize] * (V + 1)

for _ in range(E):
    start, end, w = map(int, input().split())
    adj_list[start].append((w, end))

targ, dest = map(int, input().split())


def dijkstra(start):
    pq = [(0, start)]
    visited[start] = 0

    while pq:
        d, x = heapq.heappop(pq)

        if visited[x] < d:
            continue

        for nw, nx in adj_list[x]:
            nd = d + nw

            if visited[nx] > nd:
                heapq.heappush(pq, (nd, nx))
                visited[nx] = nd


dijkstra(targ)
print(visited[dest])
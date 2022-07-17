# 2022-07-06, Sehyun Kim

import sys
sys.setrecursionlimit(10**6)

def dfs(V):
    visit[V] = 1
    result1.append(V)
    for i in board[V]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i)

# 그러나 파이썬의 list를 활용해서 tmp.pop(0)를 실행하는 건 O(n)만큼의 시간 복잡도라고 한다.
# 성능은 deque가 list보다 빠르다: https://stackoverflow.com/questions/32543608/deque-popleft-and-list-pop0-is-there-performance-difference
def bfs(V):
    visit = [0] * (N + 1)
    visit[V] = 1
    result2.append(V)
    tmp = [V]
    while tmp:
        q = tmp.pop(0)
        for i in board[q]:
            if visit[i] == 0:
                result2.append(i)
                tmp.append(i)
                visit[i] = 1
        

N, M, V = map(int, sys.stdin.readline().split())

# graph 정보를 단순한 2차원 배열에 담음으로써 메모리를 어느 정도 희생하는 대신 코드가 간단해진다
# 반면, 내 코드는 메모리를 살리기 위해 dictionary를 사용했고 그 결과 코드가 좀 길어졌다.
board = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    board[a].append(b)
    board[b].append(a)
for i in range(len(board)):
    board[i].sort()
visit = [0] * (N + 1)
result1 = []
result2 = []
dfs(V)
bfs(V)
print(*result1)
print(*result2)
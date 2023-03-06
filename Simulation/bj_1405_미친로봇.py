import sys
input = sys.stdin.readline
from collections import deque

N, *probability = map(int, input().split())
# 동서남북 순서로
probability = [prob*0.01 for prob in probability]
dx = [0,  0, 1, -1]
dy = [1, -1, 0,  0]

cnt = 0
prob = 1
start = (N, N, cnt, prob)
answer = 0


def move(x, y, visited, prob):
    # 시작점을 포함한다면, 집합 visited의 원소 개수는 이동한 횟수+1
    if len(visited) == N+1:
        return prob
    
    total_prob = 0.0
    
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if (mx,my) not in visited and probability[i] > 0:
            visited.add( (mx, my) )
            total_prob += move(mx, my, visited, prob*probability[i])
            # 다시 해제를 해주어야 각자만의 path를 구별해서 가질 수 있다.
            visited.remove( (mx, my) )
    return total_prob

# visited = set( (N,N) )
# print( move(N, N, visited, 1) )
visited = set([(N,N) for _ in range(1)])
# 또는 이것도 가능
visited = set([(N,N)])
print(move(N, N, visited, 1))
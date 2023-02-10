import sys
input = sys.stdin.readline
from collections import deque
from collections import namedtuple

Edge = namedtuple("Edge", ["v", "w"])

V, E = map(int, input().split())
# adj_list = [[]*(V+1) for _ in range(V+1)]
adj_list = [[] for _ in range(V+1)]

w_max = 1
w_min = 1000000000

for _ in range(E):
    v1, v2, w = map(int, input().split())
    adj_list[v1].append(Edge(v2, w))
    adj_list[v2].append(Edge(v1, w))
    if w > w_max:
        w_max = w
    if w < w_min:
        w_min = w

start, dest = map(int, input().split())
visited = [False]*(V+1)


def solution(left, right):
    # mid = (left + right) // 2
    global visited
    
    while left <= right:
        mid = (left + right) // 2
        
        q = deque([start])
        while q:
            curr = q.popleft()
            visited[curr] = True
            
            for adj_v in adj_list[curr]:
                if (not visited[adj_v.v]) and mid <= adj_v.w:
                    q.append(adj_v.v)

                    if adj_v.v == dest:
                        visited = [False]*(V+1)
                        return solution(mid+1, right)
        right = mid-1
        #FIXME - left, right 초기화했다면 그래프를 처음부터 다시 
        # 새로운 중량 값(mid)으로 탐색하는 것이므로 visited도 초기화해주어야 함
        visited = [False]*(V+1)
    
    # FIXME - while 문 left <= right 조건에 부합하지 않아 바로 빠져나오면
    # (left + right) // 2 값은 기존의 mid 값과 다를 수 있다
    # return mid
    return (left+right) // 2


print(solution(w_min, w_max))
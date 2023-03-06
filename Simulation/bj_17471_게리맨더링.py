import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
populations = list(map(int, input().split()))
adj_list = []
for _ in range(N):
    n, *adj_nodes = map(int, input().split())
    adj_list.append([node-1 for node in adj_nodes])
    

def diff(dA, dB):
    # dA와 dB가 리스트인 경우
    sum_dA = sum(populations[num] for num in dA)
    sum_dB = sum(populations[num] for num in dB)
    return abs(sum_dA - sum_dB)


def dfs(start, nodes):
    # visited = [False]*N
    visited = {n:False for n in nodes}
    visited[start] = True
    stack = []
    stack.append(start)
    while stack:
        cur = stack.pop()
        for adj_node in adj_list[cur]:
            # 지정한 선거구(nodes)에 포함된 노드만 순회해야 함
            if adj_node in visited and not visited[adj_node]:
                visited[adj_node] = True
                stack.append(adj_node)
    # 만약 connected component 개수가 2개 이상이라면, 다 순회하지 못함
    return not (False in visited.values())


answer = -1
for i in range(1, N//2+1):
    for comb in combinations(range(N), i):
        # REVIEW - combinations의 결과는 튜플인 점 복습하자.
        dA = list(comb)
        dB = list( set(range(N)) - set(comb) )
        
        # 둘다 순회할 수 있고 connected component 개수가 1개씩이라면:
        if dfs(dA[0], dA) and dfs(dB[0], dB):
            cur_diff = diff(dA, dB)
            if answer == -1 or answer > cur_diff:
                answer = cur_diff

print(answer)

'''
1. N은 최대 10까지니까 10C1 부터 10C5까지 combinations 조합 경우의 수 돌린 후
2. 조합으로 뽑힌 노드와 나머지 노드(이건 set으로 두 집합을 구분)에 대해 DFS 돌려서
3. 두 선거구가 모두 connected component 1개씩인 경우만 걸러낸 후,
4. 인구 차이를 구해서 (이건 또 따로 함수로 만들어야) 가장 작은 인구 차이를 답으로
'''

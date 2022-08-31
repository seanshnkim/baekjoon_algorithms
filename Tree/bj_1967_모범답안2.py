import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

'''1. Binary tree가 아니어도 성립
2. root node(1)에 2,3,4,5,6 총 5개의 child node가 있다고 하자.
1) left, right = 노드 2와 3 각각에서 dfs로 구한 최대 거리.
그리고 항상 answer에는 그 둘을 더한 것으로 업데이트하므로, 기존 bj_1967_모범답안에서처럼 dfs를 두 번 쓸 필요가 없다.
처음에는 left가 0이지만 어차피 업데이트되는 것은 right, dfs 함수가 리턴하는 것도 right이므로 상관없다.
2)엄밀히 따지면 left와 right는 왼쪽 subtree 오른쪽 subtree를 의미하는 게 아니다. 
left는 두번째로 큰 subtree, right는 가장 큰 subtree를 의미한다.
global 변수로 answer를 두는 건 어쩔 수 없는 것 같다. 결국 dfs가 반환하는 값은 가장 큰 거리이지 subtree의 지름이 아니기 때문'''

'''그리고 input의 형태는 어차피 node 번호가 1부터 순서대로 들어오는 거니까, dictionary를
쓸 필요가 없다.'''

'''이 알고리즘, 가만 분석해보니 answer라는 global 변수를 설정하고 매 스텝마다 answer 값을
갱신해나간다. 단순히 child node의 가장 큰 거리만을 구해서는 해결할 수 없는 문제이기 때문이다.
이 문제는 weight가 모두 1로 주어져있을 때와는 다른 접근 방식이 필요한 문제다.
weight가 모두 1이라면, 단순히 subtree의 깊이만을 계산하는 것이고 dfs로 해결할 수 있기 때문이다. '''

def dfs(num):
    global answer
    if graph[num]:
        left, right = 0,0
        for i, d in graph[num]:
            now_distance = dfs(i) + d
            if now_distance > right:
                left, right = right, now_distance
            elif now_distance > left:
                left = now_distance
        answer = max(answer, left+right)
        return right
    else:
        return 0

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, c = map(int, input().split())
    graph[x].append((y,c))

answer = 0
dfs(1)
print(answer)
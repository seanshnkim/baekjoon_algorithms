# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
V, E = map(int, input().split())
parent = [0] * (V+1) # 부모 테이블 초기화하기

rank = [0] * (V+1)

# parent 테이블 정보가 있다고 가정
# naive_find의 문제점: 최대 O(N) (여기서 N은 트리의 깊이)의 시간복잡도가 발생한다.
def naive_find(x):
    if parent[x] != x:
        return naive_find(parent[x])
    return x


def find(x):
    if parent[x] == x:
        return x
    else:
        root_x = find(parent[x])
        # 시간복잡도 O(N)인 naive_find의 문제점을 해결
        # 경로 압축!
        parent[x] = root_x
        return root_x


# union은 파이썬에서 이미 예약된 키워드이기 때문에, union 연산을 수행하는 함수를 대신 merge라고 하겠다.
def naive_merge(a, b):
    root_a = find(a)
    root_b = find(b)
    
    parent[root_b] = root_a


def rank_merge(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a == root_b:
        return
    
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
    
    if rank[root_a] == rank[root_b]:
        rank[root_b] += 1
         
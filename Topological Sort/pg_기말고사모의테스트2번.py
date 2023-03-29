from collections import deque, defaultdict

def solution(s1, s2, k):
    answer = []
    adj_dict = defaultdict(list)
    # FIXME - adj_dict[현재과목] = [선수과목1, 선수과목2...] 이런 식으로 짜야 한다.
    # 사실 선수과목(에서) -> 현재과목(으로)의 방향이 직관적으로 맞는 것처럼 보이지만,
    # 위상정렬 알고리즘을 이용하려면 주어진 과목 k(현재 과목)의 in_degree가 0이 되어야 하기 때문.
    # for pre, cur in zip(s1, s2):
    #     adj_dict[pre].append(cur)
    for pre, cur in zip(s1, s2):
        adj_dict[cur].append(pre)
    
    in_degrees = defaultdict(int)
    for key in adj_dict:
        # 알파벳 순으로 나중에 answer에 출력되려면, 여기선 거꾸로 내림차순으로 정렬해야 한다?
        # adj_dict[key].sort(reverse=True)
        for adj_node in adj_dict[key]:
            in_degrees[adj_node] += 1
    
    # visited = defaultdict(lambda: False)
    # visited[k] = True
    
    q = deque([k])
    while q:
        curr = q.popleft()
        # answer.appendleft(curr)
        tmp_stack = []
        tmp_stack.append(curr)
        
        for adj_node in adj_dict[curr]:
            # NOTE - visited 있어야 하나? 없어도 되는 것 같은데...
            # if not visited[adj_node]:
            in_degrees[adj_node] -= 1
            if in_degrees[adj_node] == 0:
                q.append(adj_node)
            # visited[adj_node] = True
    
    return list(answer)

s1 = ["A", "E", "B", "D", "B", "H", "F", "H", "C"]
s2 = ["G", "C", "G", "F", "J", "E", "B", "F", "B"]
K  = "B"

print(solution(s1, s2, K))

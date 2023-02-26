from collections import deque
from collections import defaultdict

def solution(tickets):
    # visited = defaultdict(int)
    adj_dict = defaultdict(list)
    vertices = set()
    for t in tickets:
        adj_dict[t[0]].append(t[1])
        vertices.add(t[0])
        vertices.add(t[1])
        # visited[t[0]] = 0
        # visited[t[1]] = 0
    # V = len(adj_dict)
    vertices = list(vertices)
    V = len(vertices)
    visited = {v:0 for v in vertices}
    
    q = deque(["ICN"])
    visited["ICN"] += 1
    path = ["ICN"]

    # FIXME - 이 조건도 틀렸다. 노드를 한번만 방문하는 게 아니기 때문에.
    # while q and len(path) < V:
    while q and (0 in visited.values()):
        curr_node = q.popleft()
        
        curr_adj_node = "ZZZZ"
        for adj_node in adj_dict[curr_node]:
            # if not visited[adj_node]:
            # visited[adj_node] = True
            # is_adjacent = True
            if visited[curr_node] == 2 and visited[adj_node] == 1:
                continue
            if adj_node < curr_adj_node:
                curr_adj_node = adj_node
        
        # # FIXME - # 만약 if문 없이 그냥 실행한다면 무한루프에 빠지게 된다.
        # if is_adjacent:
        if curr_adj_node != "ZZZZ":
            visited[curr_adj_node] += 1
            
            q.append(curr_adj_node)
            path.append(curr_adj_node)

    return path

tickets1 = [["ICN", "JFK"], 
           ["HND", "IAD"],
           ["JFK", "HND"]
           ]
tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
solution(tickets2)

# 이 문제는 BFS와 살짝 다른 게, 한번 노드를 이미 방문했다고 다시 방문 못하는 게 아니라
# 모든 노드를 순회한 후에야 종료되는 것이기 때문에 두 번이상도 방문할 수 있다.
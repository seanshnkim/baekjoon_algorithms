from collections import deque
from collections import defaultdict

def solution(tickets):
    visited = {}
    adj_dict = defaultdict(list)
    for t in tickets:
        adj_dict[t[0]].append(t[1])
        visited[t[0]] = False
        visited[t[1]] = False
    
    q = deque(["ICN"])
    visited["ICN"] = True
    path = ["ICN"]

    while q:
        curr_node = q.popleft()

        # 이게 에러의 원인
        # if visited[curr_node]:
        #     continue
        
        curr_adj_node = "ZZZ"
        is_adjacent = False
        for adj_node in adj_dict[curr_node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                is_adjacent = True
                
                if adj_node < curr_adj_node:
                    curr_adj_node = adj_node
        
        # FIXME - # 만약 if문 없이 그냥 실행한다면 무한루프에 빠지게 된다.
        if is_adjacent:
            q.append(curr_adj_node)
            path.append(curr_adj_node)
        

    return path

tickets1 = [["ICN", "JFK"], 
           ["HND", "IAD"],
           ["JFK", "HND"]
           ]
solution(tickets)
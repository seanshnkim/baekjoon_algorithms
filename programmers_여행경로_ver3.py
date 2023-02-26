from collections import deque
from collections import defaultdict

# 처음부터 문제 조건을 잘못 파악한 케이스.
# 노드가 아니라 간선을 모두 방문했는지 확인하는 문제였다.

def solution(tickets):
    E = len(tickets)
    adj_dict = defaultdict(list)
    # 파이썬에서 리스트는 딕셔너리의 키로 사용할 수 없다.
    # edges = {t:0 for t in tickets}
    
    for t in tickets:
        adj_dict[t[0]].append( [t[1], 0] )

    q = deque([ "ICN" ])
    path = ["ICN"]
    
    while q and len(path) <= E:
        curr_node = q.popleft()
        
        curr_adj_node = "ZZZZ"
        idx_curr_adj_node = 0
        # for adj_node in adj_dict[curr_node]:
        for i in range(len(adj_dict[curr_node])):
            adj_node = adj_dict[curr_node][i]
            
            # if adj_dict[adj_node][1] > 0:
            if adj_dict[curr_node][i][1] > 0:
                continue
            if adj_node[0] < curr_adj_node:
                curr_adj_node = adj_node[0]
                idx_curr_adj_node = i
        
        if curr_adj_node != "ZZZZ":
            q.append(curr_adj_node)
            path.append(curr_adj_node)
            adj_dict[curr_node][idx_curr_adj_node][1] += 1
            

    return path 

tickets1 = [["ICN", "JFK"], 
           ["HND", "IAD"],
           ["JFK", "HND"]
           ]
tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
solution(tickets2)

# 이 문제는 BFS와 살짝 다른 게, 한번 노드를 이미 방문했다고 다시 방문 못하는 게 아니라
# 모든 노드를 순회한 후에야 종료되는 것이기 때문에 두 번이상도 방문할 수 있다.
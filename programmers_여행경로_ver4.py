from collections import defaultdict

# FIXME - cycle이 존재하기 때문에 이런 코드로는 X
# def dfs(start):
#     curr_adj_node = "ZZZZ"
#     for adj_node in adj_dict[start]:
#         if adj_node < curr_adj_node:
#             curr_adj_node = adj_node
    
#     if curr_adj_node == "ZZZZ":
#         return [start]
    
#     return [start] + dfs(curr_adj_node)


# adj_dict = defaultdict(list)
# def solution(tickets):
#     for t in tickets:
#         adj_dict[t[0]].append(t[1])
    
#     return dfs("ICN")


def dfs(start):
    curr_adj_node = "ZZZZ"
    idx_curr_adj_node = 0
    for idx in range(len(adj_dict[start])):
    # for adj_node in adj_dict[start]:
        adj_node = adj_dict[start][idx]
        # e.g. adj_node = ["SFO", False]
        if adj_node[1]:
            continue
        if adj_node[0] < curr_adj_node:
            curr_adj_node = adj_node[0]
            idx_curr_adj_node = idx
            
    
    if curr_adj_node == "ZZZZ":
        return [start]
    
    adj_dict[start][idx_curr_adj_node][1] = True
    
    return [start] + dfs(curr_adj_node)


adj_dict = defaultdict(list)
def solution(tickets):
    for t in tickets:
        adj_dict[t[0]].append([t[1], False])
    
    return dfs("ICN")


solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])

# 반례: https://eocoding.tistory.com/68
# ICN -> A,
# ICN -> B,
# B -> ICN
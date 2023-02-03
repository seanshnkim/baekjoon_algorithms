import sys

V, E = map(int, sys.stdin.readline().split())
adj_matrix = [[False]*V for _ in range(V)]
adj_list = [[] for _ in range(V)]
edge_list = []

for e in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj_matrix[v1][v2] = adj_matrix[v2][v1] = True
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)
    edge_list.append((v1, v2))
    edge_list.append((v2, v1))


def search(adj_matrix, adj_list, edge_list):
    E_doubled = len(edge_list)
    for i in range(E_doubled):
        for j in range(E_doubled):
            if i == j:
                continue
            A, B = edge_list[i]
            C, D = edge_list[j]
            if A == B or A == C or A == D or B == C or B == D or C == D:
                continue
            if adj_matrix[B][C]:
                for E in adj_list[D]:
                    if E != A and E != B and E != C and E != D:
                        return 1
    return 0


print(search(adj_matrix, adj_list, edge_list))
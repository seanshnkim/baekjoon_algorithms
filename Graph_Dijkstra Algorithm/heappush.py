import heapq

input_list = [(2, 2), (3, 3), (10, 5), (3, 5)]
pq = []

for i in input_list:
    heapq.heappush(pq, i)

print(pq)
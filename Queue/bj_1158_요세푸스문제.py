import sys
input = sys.stdin.readline
# from collections import deque

N, K = map(int, input().split())

# q = deque([i for i in range(1, N+1)] )
# answer = []
# while q:
#     for i in range(K-1):
#         q.append(q.popleft())
#     answer.append(q.popleft())

input_str = [i for i in range(1, N+1)]
# del_idx = K-1
del_idx = 0
answer = []
while input_str:
    del_idx += K-1
    curr_len = len(input_str)
    if del_idx >= curr_len:
        del_idx %= curr_len
    answer.append(input_str.pop(del_idx))

print('<', ', '.join(map(str, answer) ), '>', sep='')
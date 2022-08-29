import sys
from collections import deque

len_queue, n_select = map(int, sys.stdin.readline().split())
loc_list = list(map(int, sys.stdin.readline().split()))
loc_queue = deque([i for i in range(1, len_queue+1)])

cnt = 0
curr_len = len_queue
for loc in loc_list:
    if loc_queue.index(loc) <= curr_len // 2:
        while loc_queue[0] != loc:
            loc_queue.append(loc_queue.popleft())
            cnt += 1
    else:
        while loc_queue[0] != loc:
            loc_queue.appendleft(loc_queue.pop())
            cnt += 1
    loc_queue.popleft()
    curr_len -= 1

print(cnt)


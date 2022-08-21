import sys

n_queue, n_people = map(int, sys.stdin.readline().split())

t_per_queue = []

for _ in range(n_queue):
    t_per_queue.append(int(sys.stdin.readline()))

start = 0
end = max(t_per_queue) * n_people

while start <= end:
    mid = (start + end) // 2
    cnt_avail_people = sum([mid // x for x in t_per_queue])

    if cnt_avail_people >= n_people:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)
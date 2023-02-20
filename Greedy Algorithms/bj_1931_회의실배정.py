import sys
input = sys.stdin.readline
from collections import namedtuple
Conf_time = namedtuple("conf_time", ["start", "end"])

N = int(input())
times = [Conf_time(*map(int, input().split())) for _ in range(N)]

times.sort(key=lambda x: (x.end, x.start) )

cnt = 1
curr_end = times[0].end
for t in times:
    # 끝나는 시간을 기준으로 정렬했으므로 for 문 순회가 가능
    if t.start >= curr_end:
        curr_end = t.end
        cnt += 1

print(cnt)
    
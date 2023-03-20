import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
memories = list(map(int, input().split()))
inact_mem = list(map(int, input().split()))

answer = float('inf')
for i in range(1, N+1):
    for comb in combinations(range(N), r=i):
        if sum(memories[i] for i in comb) >= M:
            sum_inact = sum(inact_mem[i] for i in comb)
            answer = min(answer, sum_inact)

print(answer)
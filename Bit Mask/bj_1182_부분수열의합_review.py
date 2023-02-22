import sys
input = sys.stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))

answer = 0
for i in range(1, 1<<N):
    curr_sum = 0
    for j in range(N):
        if i & (1<<j) != 0:
            curr_sum += seq[j]
    if curr_sum == S:
        answer += 1

print(answer)
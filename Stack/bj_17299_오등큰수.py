import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
sequence = list(map(int, input().split()))
counts = Counter(sequence)
stack = [0]
answer = [-1]*N


for idx in range(1, N):
    while stack and counts[sequence[stack[-1]]] < counts[sequence[idx]]:
        top = stack[-1]
        answer[top] = sequence[idx]
        stack.pop()
    stack.append(idx)

print(*answer)
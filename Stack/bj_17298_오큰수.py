import sys
input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))

stack = [0]
answer = [-1]*N


for idx in range(1, N):
# 이렇게 하면 무한루프를 돌게 된다.
#     while stack:
#         top = stack[-1]
#         if sequence[top] < sequence[idx]:
    while stack and sequence[stack[-1]] < sequence[idx]:
        top = stack[-1]
        answer[top] = sequence[idx]
        stack.pop()
    stack.append(idx)

print(*answer)
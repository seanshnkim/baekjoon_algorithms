import sys
input = sys.stdin.readline

N = int(input())
output = [int(input().rstrip('\n')) for _ in range(N)]

i = N-1
stack = []
ans = []
latest = N+1
while i >= 0:
    if i == N-1:
        stack.append(output[i])
        ans.append('-')
        i -= 1
        continue
    while stack and output[i] > stack[-1]:
        stack.append(output[i])
        ans.append('-')
        i -= 1
    if i < 0:
        break
    # if output[i] < stack[-1]이 포함
    while stack and output[i] < stack[-1]:
        curr = stack.pop()
        if curr > latest:
            print("NO")
            sys.exit(0)
        
        latest = min(latest, curr)
        ans.append('+')
        
    stack.append(output[i])
    i -= 1

while stack:
    ans.append('+')
    stack.pop()
    
print(*ans[::-1], sep='\n')

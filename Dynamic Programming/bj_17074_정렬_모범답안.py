import sys
input = sys.stdin.readline

N = int(input())
numbers = [-float('inf')] + list(map(int, input().split())) + [float('inf')]

ans = 0
cnt = 0
prev = 0
post = 0

for i in range(1, N+1):
    
    if numbers[i] < numbers[i-1]:
        cnt += 1
        prev = i - 1
        post = prev + 1

if cnt == 0:
    ans = N
elif cnt > 1:
    ans = 0
else:
    if numbers[prev-1] <= numbers[post]:
        ans += 1
    if numbers[prev] <= numbers[post+1]:
        ans += 1

print(ans)
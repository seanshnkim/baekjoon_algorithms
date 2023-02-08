import sys
input = sys.stdin.readline
from collections import namedtuple
Pair = namedtuple('Pair', ['left', 'right'])

N = int(input())
pairs = []
for _ in range(N):
    pairs.append(Pair(*map(int, input().split())) )

pairs = sorted(pairs, key=lambda x: x.left)

prev = pairs[0]
ans = prev.right - prev.left
for i in range(1, N):
    curr = pairs[i]
    if curr.left <= prev.right:
        ans -= (prev.right - curr.left)
        ans += (curr.right - curr.left)
        prev = Pair(prev.left, curr.right)
        
    elif curr.left > prev.right:
        ans += (curr.right - curr.left)
        prev = curr

print(ans)

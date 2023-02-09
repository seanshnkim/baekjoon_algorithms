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
    # FIXME 
    # if curr.left <= prev.right: -> 만 붙이면 아래 반례를 통과하지 못한다.
    # 즉, curr.left <= prev.right 이고 curr.right < prev.right 일 때 문제가 발생한다.
    if curr.left <= prev.right and curr.right > prev.right:
        ans -= (prev.right - curr.left)
        ans += (curr.right - curr.left)
        prev = Pair(prev.left, curr.right)
        
    elif curr.left > prev.right:
        ans += (curr.right - curr.left)
        prev = curr

print(ans)

'''
반례:
4
5 10
15 20
25 30
7 35

output: 20
answer: 30
'''

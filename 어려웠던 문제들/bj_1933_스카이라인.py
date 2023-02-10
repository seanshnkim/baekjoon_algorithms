import sys
from collections import namedtuple
input = sys.stdin.readline
Building = namedtuple('Building', ['left', 'height', 'right'])
Pair = namedtuple('Pair', ['x', 'height'])


def ans_check(ans: [Pair], p: Pair):
    if ans:
        # x는 해당 height가 유지되는, 시작점을 의미
        # 따라서 height가 같다면 x를 따로 추가할 필요가 X
        if ans[-1].height == p.height:
            return
        # height가 다르다면, 그리고 x가 같다면 height 자체를 수정해야 한다
        if ans[-1].x == p.x:
            ans[-1] = Pair(ans[-1].x, p.height)
            return
    # x좌표 값도 다르고(항상 같거나 큰 x좌표값만 들어온다) height도 다르다면 
    # 그냥 ans에 추가한다
    ans += [p]


def merge(l: [Pair], r: [Pair]):
    ans = []
    h1 = h2 = 0
    i = j = 0
    
    while i < len(l) and j < len(r):
        u, v = l[i], r[j]
        
        if u.x < v.x:
            x = u.x
            h1 = u.height
            ans_check(ans, Pair(x, max(h1, h2) ))
            i += 1
        else:
            x = v.x
            h2 = v.height
            # h1에 바로 이전 height 정보를 저장해둔다.
            # 만약 여전히 h1이 현재 height인 h2보다 크다면, h1을 저장한다.
            ans_check(ans, Pair(x, max(h1, h2)))
            j += 1

    while i < len(l):
        ans_check(ans, l[i])
        i += 1

    while j < len(r):
        ans_check(ans, r[j])
        j += 1

    return ans


def solution(a: [Building], start, end):
    if start == end:
        return [
            Pair(a[start].left, a[start].height),
            Pair(a[start].right, 0)
        ]

    mid = (start + end) // 2
    l = solution(a, start, mid)
    r = solution(a, mid+1, end)

    return merge(l, r)


N = int(input())
buildings = [Building(*map(int,input().split())) for _ in range(N)]
# 꼭 left x좌표 값 기준으로 정렬해줘야 함. 머지 소트의 사전조건: 정렬된 배열
buildings.sort()
res = solution(buildings, 0, N-1)

answer = []
for x, h in res:
    answer.extend([x, h])

print(*answer)
import sys
input = sys.stdin.readline
N = int(input())


def is_attackable(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2
    return abs(x1-x2) == abs(y1-y2) or x1 == x2 or y1 == y2


# N*N 크기의 격자판에서, N개의 퀸이 서로 공격당하지 않으려면
# 비둘기 집의 원리에 의해 각 행마다 하나씩 배치할 수밖에 없다.
def solution(cur_row, prev_loc):
    cnt = 0
    if cur_row == N-1:
        return 1
    
    else:
        for y in range(N):
            is_attacked = False
            cur_loc = (cur_row+1, y)
            
            for loc in prev_loc:
                if is_attackable(cur_loc, loc):
                    is_attacked = True
                    break
            if not is_attacked:
                cnt += solution( cur_row+1, prev_loc+[cur_loc] )
        return cnt


if N == 1:
    print(1)
else:
    answer = 0
    for i in range(N):
        answer += solution(0, [(0,i)])
    print(answer)


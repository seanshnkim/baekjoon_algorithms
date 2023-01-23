import sys

N = int(sys.stdin.readline())

days = []
profits = []
for _ in range(N):
    h, p = map(int, sys.stdin.readline().split())
    days.append(h)
    profits.append(p)


def solution(d, sum, p):
    if d > N:
        # 이미 day가 초과해서 상담을 할 수 없는 것이므로
        # profit은 증가하지 않고 그대로
        return sum - p
    if d == N:
        return sum
    
    # 현재 day에서 상담을 할 경우 vs. 현재 day에서 상담하지 않고 다음 날 선택
    return max(solution(d+days[d], sum+profits[d], profits[d]), \
               solution(d+1, sum, 0))
    
print(solution(0, 0, 0))

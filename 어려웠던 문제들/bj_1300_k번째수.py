import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

#FIXME - (k//N)*N의 의미는 B[x] = k이면 x는 최소한 (k//N)*N이라는 뜻으로,
# 잘못 파악한 것
# left = (k//N)*N
left = 0
right = N*N
answer = (left + right) // 2

while left <= right:
    mid = (left + right) // 2

    # 만약 B[x] = mid라면, x는 최소한 [1][1~N] ~ [mid//N][1~N] -> N*(mid//N)개 이상이라는 뜻
    # 즉 [i][1~N] 행 전체 원소가 모두 mid보다 작은 경우의 수를 구하는 것
    cnt = (mid//N) * N
    for i in range(mid//N+1, min(mid, N)+1):
        # cnt += min(k//i, N)이 아니다.
        cnt += mid//i
    if cnt >= k:
        answer = mid
        right = mid-1
    else:
        left = mid+1

print(answer)
'''
반례:
5
8
output: 5
answer: 4
'''
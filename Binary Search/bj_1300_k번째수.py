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
    '''
    여기서 cnt는 배열 B에서 B[x] = mid일 때 x의 값을 말한다.
    예를 들어 mid = 15, N = 5 라면 행 index가 1,2,3인 경우에 대해서는 
    행 전체 원소(A[1][1~N], A[2][1~N], A[3][1~N])가 모두 15보다 작을 것이다.
    만약 어떤 행 A[i][k]에 대해 A[i][N]이 mid보다 작거나 같다면, A[i][N]이 i번째 행에서
    제일 큰 원소이기 때문에 i번째 행 원소 전체(N개)가 모두 mid보다 작다는 걸 알 수 있다.
    따라서 A[i][N]이 mid보다 작거나 같은지 판단한 후,
    => if i <= mid//N 
    then i번째 행에 대해서는 모두 cnt += N씩 해준다
    => cnt += N (cnt의 초기값은 0)
    
    더 간단하게 하자면, 매번 i=1,2,3...mid//N에 대해 
    cnt에 N을 더하지 않고 한번에 곱셈해서 초기값을 설정하면 된다
    => cnt = (mid//N) * N
    '''
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
import sys
input = sys.stdin.readline

N = int(input())
matrices = [tuple(map(int, input().split())) for _ in range(N)]

# dp[n][k] = V : n번째 행렬부터 k번째 행렬까지 곱했을 때 최소 곱셈 연산 수
dp = [[0]*N for _ in range(N)]
# products[n][k] = V : n번째 행렬부터 k번째 행렬까지 곱했을 때, 결과로 나오는 한 행렬의 행*열 곱한 결과
products = [[0]*N for _ in range(N)]
    
for i in range(N):
    for j in range(i, N):
        products[i][j] = matrices[i][0] * matrices[j][1]

for i in range(N-1):
    dp[i][i+1] = products[i][i] * matrices[i+1][1]


def dfs(s, e):
    if e - s <= 1:
        return
    
    cur_min = dp[s][e]
    
    for i in range(e-s):
        if dp[s][s+i] == 0:
            dfs(s, s+i)
        if dp[s+i+1][e] == 0:
            dfs(s+i+1, e)
        
        cur_prod = dp[s][s+i] + dp[s+i+1][e] + products[s][s+i] * matrices[e][1]
        if cur_min == 0 or cur_min > cur_prod:
            cur_min = cur_prod
    
    dp[s][e] = cur_min
    return

dfs(0, N-1)
print(dp[0][-1])

'''
반례:
5
1 10
10 1
1 10
10 1
1 10
정답: 31
출력: 40
'''
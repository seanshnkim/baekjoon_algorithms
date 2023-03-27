import sys
input = sys.stdin.readline

LIMIT = 100
N = int(input())
costs =   list(map(int, input().split()))
profits = list(map(int, input().split()))

# dp[n][l] = V -> 0 ~ n번째 cost 골라서 l만큼의 체력을 소모하여(100에서 뺀 값 아님) 얻을 수 있는 최대 profit V
dp = [[0]*LIMIT for _ in range(N)]

if costs[0] < LIMIT:
    # 이 아이디어가 중요하다. 
    # dp[0][costs[0]] ~ dp[0][99] = profits[0] -> 즉, cost를 정확히 'x만큼' 소모하여 얻을 수 있는 최대 profit 값이 아니라,
    # cost를 x '이상' 소모했을 때 얻을 수 있는 최대 profit 값을 dp 배열 값으로 지정해야 한다.
    for c in range(costs[0], LIMIT):
        dp[0][c] = profits[0]


for i in range(1, N):
    cost, profit = costs[i], profits[i]
    for c in range(LIMIT):
        if c - cost >= 0:
            # dp[i] 배열은 0부터 i번째 cost를 각각 적어도 하나 사용하거나, 또는 사용하지 않는 경우를 모두 포함한다.
            dp[i][c] = max(dp[i-1][c], dp[i-1][c-cost]+profit)
        
        else:
            dp[i][c] = dp[i-1][c]

print(dp[-1][-1])

'''
8
100 26 13 17 24 33 100 99
34 56 21 1 24 34 100 99

-> 정답은 (26, 56), (13, 21), (24, 24), (33, 34) 를 골라서 -> 135가 된다.

이때 1) costs에서 순차적으로 무조건 꼭 하나씩 골라야 한다면,
답은 (26, 56), (13, 21), (17, 1), (24, 24) -> 102가 된다.

(3번째 cost는 (17,1)이다)
dp[3][43] = dp[3][39] -> 17을 고르지 않았다
dp[3][63] = ...dp[2][63]과 dp[2][46]+1 중 비교 -> dp[2][46]+1이 되고, dp[3][63]은 26,13,17을 모두 고른 셈이 된다.
dp[4][63] = dp[3][63] vs. dp[3][39]과 비교
            dp[3][39] 은 17을 고르지 않았다 -> 여기에 현재 profit 24 더한 것 (101)
            dp[3][63]은 17을 골라서 63까지 만든 것이다 (78)
            따라서 101이 된다.
dp[5][96] = dp[4][96] vs. dp[4][63]+34
'''
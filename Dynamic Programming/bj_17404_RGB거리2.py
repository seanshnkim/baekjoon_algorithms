'''
1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
costs = []
costs = [list(map(int, input().split())) for _ in range(N)]

# for i in range(3):
#     # dp[0]에 대해서는 왼쪽 칸이 없다고 가정하자
#     dp[0][i][0] = costs[0].red
#     dp[0][i][1] = costs[0].green
#     dp[0][i][2] = costs[0].blue


# for i in range(1, N-1):
#     for c_prev in range(3):
#         for c_cur in range(3):
#             for j in range(3):
#                 if dp[i-1][j][c_prev] > 0 and c_prev != c_cur:
#                     dp[i][c_prev][c_cur] = dp[i-1][j][c_prev] + costs[i][c_cur]

# NOTE: 이렇게 풀게 되면 0번째 칸이 red일 때, blue일 때, green일 때 일일이 다시 추적해야 한다.
# 즉, dp[N-1]을 업데이트하게 됐을 때는 dp[N-2], dp[N-3]... dp[1] 이 모두 0번째 칸의 색깔 정보를 기억하고 있는 게 아니다.
# -> 그렇다면 단순하게 생각: 어차피 색깔은 해봤자 3가지니까, 처음부터 0번째 칸의 색깔을 고정해놓고 dp 배열을 모두 업데이트한 다음 값을 구해서
# 이렇게 0번째 칸을 red, green, blue 3가지 색깔로 칠했을 때 나오는 결과값을 비교만 하면 된다.

def simulate(init_col):
    dp = [[float('inf')]*3 for _ in range(N)]
    dp[0][init_col] = costs[0][init_col]

    for i in range(1, N):
        for c_cur in range(3):
            for c_prev in range(3):
                if c_prev != c_cur and dp[i-1][c_prev] != float('inf'):
                    dp[i][c_cur] = min(dp[i][c_cur], dp[i-1][c_prev])
            if dp[i][c_cur] != float('inf'):
                dp[i][c_cur] += costs[i][c_cur]
    
    
    if init_col == 0:
        min_cost = min(dp[-1][1], dp[-1][2])
    elif init_col == 1:
        min_cost = min(dp[-1][0], dp[-1][2])
    else:
        min_cost = min(dp[-1][0], dp[-1][1])
    
    return min_cost


answer = float('inf')
for color in range(3):
    answer = min(answer, simulate(color))
print(answer)
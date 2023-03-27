'''
1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.
'''

import sys
from collections import namedtuple
input = sys.stdin.readline

Color = namedtuple("Color", ["red", "green", "blue"])
N = int(input())
costs = []
for _ in range(N):
    costs.append(Color(*map(int, input().split())))

# dp[n][m][k][l] = V -> n: n번째 집 / m(0~2): n번째 집이 각각 red(0), green(1), blue(2)일 때
# k(0~2): n-1번째 집(0번째 집에 대해서는 n번째 집을 의미)이 각각 red, green, blue일 때
# l(0~2):  n+1번째 집(n번째 집에 대해서는 0번째 집을 의미)이 각각 red, green, blue일 때
dp = [[[[0]*3
        for _ in range(3)]
       for _ in range(3)] 
      for _ in range(N)]


color_num_set = set([0,1,2])
for c in range(3):
    rest = list(color_num_set - {c})
    for k in range(2):
        for m in range(2):
            dp[0][c][rest[k]][rest[m]] = costs[0][c]


def return_min(idx_prev, prev, cur):
    cur_min = float('inf')
    for i in range(3):
        tmp = dp[idx_prev][prev][i][cur]
        if tmp > 0 and tmp < cur_min:
            cur_min = tmp
    return cur_min


for i in range(1, N-1):
    for c in range(3):
        rest = list(color_num_set - {c})
        for k in range(2):
            for m in range(2):
                dp[i][c][rest[k]][rest[m]] = return_min(i-1, rest[k], c)
                if dp[i][c][rest[k]][rest[m]] > 0:
                    dp[i][c][rest[k]][rest[m]] += costs[i][c]
                # 현재 칸의 color c는 dp[i-1][*][X][*] X와 같을 때에 가져온다.
                # 현재 칸(n번째) idx / 현재 color / n-1번째 color / n+1번째 color
                
                    
# dp[N-1]에 대해서는 별도로 처리해야
'''
dp[N-1][0]
'''

for c in range(3):
    rest = list(color_num_set - {c})
    for k in range(2):
        for m in range(2):
            # FIXME
            # dp[N-1][c][rest[k]][rest[m]] = 0
            cur_min = float('inf')
            for j in range(3):
                for p in range(3):
                    tmp1 = dp[0][rest[k]][c][j]
                    tmp2 = dp[N-2][rest[m]][p][c]
                    if tmp1 > 0:
                        cur_min = min(cur_min, tmp1)
                    if tmp2 > 0:
                        cur_min = min(cur_min, tmp2)
                        
            if cur_min != float('inf'):
                dp[N-1][c][rest[m]][rest[k]] = cur_min
                dp[N-1][c][rest[m]][rest[k]] += costs[N-1][c]


ans = float('inf')
for c in range(3):
    for k in range(3):
        for m in range(3):
            if dp[N-1][c][k][m] > 0 and ans > dp[N-1][c][k][m]:
                ans = dp[N-1][c][k][m]
print(ans)

'''
dp[N-1][0] -> (dp[0][1][0][j], dp[N-2][2][k][0])
              (dp[0][1][0][j], dp[N-2][1][k][0])
              (dp[0][2], dp[N-2][1])
              (dp[0][2], dp[N-2][2])
dp[N-1][0] -> dp[0][]
dp[0][1]
'''
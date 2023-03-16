import sys
input = sys.stdin.readline

N = int(input())
matrices = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
for i in range(N-1):
    dp[i][i] = [0, matrices[i][0], matrices[i][1]]
    cur_sum = matrices[i][0] * matrices[i][1] * matrices[i+1][1]
    dp[i][i+1] = [cur_sum, matrices[i][0], matrices[i+1][1]]
dp[-1][-1] = [0, matrices[-1][0], matrices[-1][1]]


def solution(s, e):
    if e - s <= 1 or dp[s][e][0] != 0:
        return dp[s][e]
    
    ans = -1
    for i in range(e-s):
        sum1, *mat1 = solution(s, s+i)
        sum2, *mat2 = solution(s+i+1, e)
        
        cur_sum = sum1 + sum2 + mat1[0] * mat1[1] * mat2[1]
        if ans == -1 or cur_sum < ans:
            ans = cur_sum
            dp[s][e] = [ans, mat1[0], mat2[1]]
    
    return dp[s][e]


print(solution(0, N-1)[0])

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
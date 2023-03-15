import sys
input = sys.stdin.readline

N = int(input())
matrices = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[[-1,-1,-1,-1] for _ in range(N)] for _ in range(N)]

def solution(s, e):
    if -1 not in dp[s][e]:
        return dp[s][e]
    
    if e - s == 1:
        cur_sum = matrices[s][0] * matrices[s][1] * matrices[e][1]
        dp[s][e] = [cur_sum, matrices[s][0], matrices[s][1], matrices[e][1]]
        return dp[s][e]
    
    sum1, *res1 = solution(s, e-1)
    sum2, *res2 = solution(s+1, e)
    
    ans1 = sum1 + res1[0] * matrices[e][0] * matrices[e][1]
    ans2 = sum2 + matrices[s][0] * matrices[s][1] * res2[2]
    
    if ans1 < ans2:
        dp[s][e] = [ans1, res1[0], matrices[e][0], matrices[e][1]]
    else:
        dp[s][e] = [ans2, matrices[s][0], matrices[s][1], res2[2]]
    
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
import sys
input = sys.stdin.readline

N = int(input())
matrices = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[[-1,-1,-1,-1] for _ in range(N)] for _ in range(N)]

def solution(s, e):
    if s == e:
        return [0, matrices[s][0], matrices[s][1]]
    
    if -1 not in dp[s][e]:
        return dp[s][e]
    
    if e - s == 1:
        cur_sum = matrices[s][0] * matrices[s][1] * matrices[e][1]
        dp[s][e] = [cur_sum, matrices[s][0], matrices[e][1]]
        return dp[s][e]
    
    ans = -1
    for i in range(e-s):
        sum1, *res1 = solution(s, s+i)
        sum2, *res2 = solution(s+i+1, e)
        
        cur_sum = sum1 + sum2 + res1[0]*res1[1]*res2[1]
        if ans == -1 or cur_sum < ans:
            ans = cur_sum
            dp[s][e] = [ans, res1[0], res2[1]]
    
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
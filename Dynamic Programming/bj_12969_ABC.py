import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# dp[numA][numB][numC][마지막 알파벳][마지막에서 두번째 알파벳] = k
# 차례로 N+1, N+1, N+1, 3, 3 크기
# dp = [ X for _ in range(N+1)]
# X =  [ Y for _ in range(N+1)]
# Y =  [ Z for _ in range(N+1)]


dp = [ [ [ ['']*(K+1)
           for _ in range(N+1)]
        for _ in range(N+1)]
      for _ in range(N+1)]

dp[1][0][0][0] = 'A'
dp[0][1][0][0] = 'B'
dp[0][0][1][0] = 'C'

for a in range(N+1):
    for b in range(N+1):
        for c in range(N+1):
            if a + b + c > N:
                break
            if a > 0:
                # 이거 시간 복잡도를 줄일 방법이 있을까?
                for p in range(K+1):
                # A를 붙인 경우
                    if dp[a-1][b][c][p] != '':
                        dp[a][b][c][p] = dp[a-1][b][c][p] + 'A'
            
            if b > 0:
                for p in range(K+1):
                    if dp[a][b-1][c][p] != '':
                        if p+a <= K:
                            dp[a][b][c][p+a] = dp[a][b-1][c][p] + 'B'
            
            if c > 0:
                for p in range(K+1):
                    if dp[a][b][c-1][p] != '':
                        if p+a+b <= K:
                            dp[a][b][c][p+a+b] = dp[a][b][c-1][p] + 'C'

def solution():
    for a in range(N+1):
        for b in range(N+1):
            c = N - (a+b)
            if c >= 0 and dp[a][b][c][K] != '':
                    return dp[a][b][c][K]
    return -1

print(solution())

'''
A -> A + A 
     A + B dp[1][1][0][1][0] = 1
     A + C dp[1][0][1][2][0] = 1
      
B -> B + A dp[1][1][0][1][0] = 0
     B + B dp[0][2][0][1][1] = 0
     B + C dp[0][1][1][1][2] = 1
     
C -> C + A
     C + B
     C + C
     
저렇게 쭉 이어질 거고,
N = 10, K = 5라고 주어졌다고 해보자.
N = 10을 만족하는 numA, numB, numC 조합에 대해 모두 dp 배열 시도해본다.
예)
'''
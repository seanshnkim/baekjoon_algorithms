import sys
input = sys.stdin.readline

records = input().rstrip('\n')
LENGTH = len(records)

numA = records.count('A')
numB = records.count('B')
numC = LENGTH - (numA+numB)

# L <= 50 -> 최대 크기: 125000
# -1 : 업데이트 X
# inner_list = [['']*3 for _ in range(3)]
# dp = [i][j][k][pp][p]

dp = [ [ [ [
              ['']*3 
            for _ in range(3)] 
          for _ in range(numC+1)] 
        for _ in range(numB+1)] 
      for _ in range(numA+1)]

for i in range(3):
    if numA > 0:
        dp[1][0][0][0][i] = 'A'
    if numB > 0:
        dp[0][1][0][1][i] = 'B'
    if numC > 0:
        dp[0][0][1][2][i] = 'C'



for a in range(numA+1):
    for b in range(numB+1):
        for c in range(numC+1):
            if a > 0:
                # dp[a][b][c] <- A를 붙이는 경우
                for i in range(3):
                    # dp[A][B][C][마지막 문자(0 -> A, 1 -> B, 2 -> C)][두번째 마지막 문자]
                    # 바로 그 이전 문자열 *...*X + A -> 
                    # sum을 하면 안되고, 가능한 문자열만 솎아내서? 근데 가능한 문자열 중에 만약에 그 다음이 안되는 거면?
                    # 일단 모르겠고 한번 해보자.
                    # dp[a][b][c][0][i] = sum(dp[a-1][b][c][i])
                    for j in range(3):
                        if dp[a-1][b][c][i][j] != '':
                            dp[a][b][c][0][i] = dp[a-1][b][c][i][j] + 'A'
            if b > 0:
                # ....AB <- ...AA + B 또는 ...BA + B 또는 ...CA + B. 3가지 모두 가능
                # ....BB <- 땡!
                # ....CB <- ...AC + B 또는 ...BC + B 또는 ...CC + B 3가지 모두 가능
                # dp[a][b][c][B][A]
                for i in range(3):
                    for j in range(3):
                        # 바로 이전 문자가 B이면 B를 붙일 수 없지만(i != 1), B를 처음으로 쓰는 것이라면(b == 1) B를 붙이는 게 가능하다.
                        if b == 1 or i != 1:
                            if dp[a][b-1][c][i][j] != '':
                                # *...*X + B -> *...*
                                dp[a][b][c][1][i] = dp[a][b-1][c][i][j] + 'B'
                        
            if c > 0:
                # ....AC <- ...AA + C 또는 ...BA + C. ///// ...CA + C는 불가능.
                # ....BC <- ...AB + C. ///// ...BB + C 와 ...CB + C는 불가능.
                # for i in range(3):
                #     if i == 2:
                #         continue
                #     for j in range(3):
                #         if j == 2:
                #             continue
                #         if dp[a][b][c-1][i][j] != '':
                #             dp[a][b][c][2][i] = dp[a][b][c-1][i][j] + 'C'
                for i in range(3):
                    for j in range(3):
                        if c == 1 or (i != 2 and j != 2):
                            if dp[a][b][c-1][i][j] != '':
                                dp[a][b][c][2][i] = dp[a][b][c-1][i][j] + 'C'
                                '''
                                기존 문자열: ABCBABC + C
                                '''
                
'''
a+b+c = N을 만족하는 0 이상의 정수 a,b,c 해 가짓수 -> 중복순열?
N을 n, a,b,c -> 숫자 개수를 k라 하자. 이때 k = 3
위 경우의 수는 N개의 (같은) 공과 k-1개의 (같은) bar(a,b,c 세 숫자를 구분하기 위한 용도. m개의 숫자를 구분하려면 m-1개의 bar만 있으면 된다)
를 배열하는 방법과 같으므로,
combination(N=n+k-1, R=k-1)과 같다.
'''
def solution():
    for i in range(3):
        for j in range(3):
            if dp[numA][numB][numC][i][j] != '':
                return dp[numA][numB][numC][i][j]
    return -1

print(solution())
'''
예를 들어서 CABCABBA 이면 
numA = 3
numB = 3
numC = 2

dp[0][0][0] ... dp[3][3][2]
dp[2][2][2][0][1] -> numA = 2이고, numB = 2이고, numC = 2일 때,
바로 전 글자가 0번째 알파벳(A)이고 전전 글자가 1번째 알파벳(B)인 가능한 문자열?
AABBCC로 만들 수 있는 조합 중에... CABCBA 쯤이 되겠다
그럼 바로 전 글자가 A니까 그 다음에 올 글자는 A,B,C 아무거나 가능
만약 전 글자가 B이면 B는 그 다음에 못 올 거고
전전 글자가 C이거나 전 글자가 C이면 C는 그 다음에 못 올 거고
'''
'''
정수 N과 K가 주어졌을 때, 다음 두 조건을 만족하는 문자열 S를 찾는 프로그램을 작성하시오.

문자열 S의 길이는 N이고, 'A', 'B', 'C'로 이루어져 있다.
문자열 S에는 0 ≤ i < j < N 이면서 S[i] < S[j]를 만족하는 (i, j) 쌍이 K개가 있다.

첫째 줄에 문제의 조건을 만족하는 문자열 S를 출력한다. 가능한 S가 여러 가지라면, 아무거나 출력한다. 만약, 그러한 S가 존재하지 않는 경우에는 -1을 출력한다.
'''

'''
ABC -> N = 3, K = 3
ABCA -> N = 4, K = 3 4번째 문자 정보: (num_A=1+1, num_B=1, num_C=1)
ABCB -> N = 4, K = 3+1
ABCC -> N = 4, K = 3+2
ABCAA -> N = 5, K = 3
ABCAB -> N = 5, 4번째 문자 정보: (num_A=0, num_B=1, num_C=1) -> 정보를 이용,
         5번째 문자 B는 B > A이므로 5번째 문자 정보: (num_A=num_A[4], num_B=num_B[1]+1, num_C=num_C[4])
         
dp = [[0,1,2] for _ in range(N)]이라 하고,
dp[n][0] -> n번째 자리에서 A를 고른 경우
dp[n][1] -> n번째 자리에서 B를 고른 경우
dp[n][2] -> n번째 자리에서 C를 고른 경우

반대로 0 ≤ i < j < N 이면서 S[i] < S[j]를 만족하는 (i, j) 쌍이 k개가 있는 문자열을 먼저 가정해보자.
k = 1 : AB,     BC,           AC,
        AB+A, / BC+A, BC+B, / AC+A
        C+AB, B+AB,
        C+BC,
        C+AC,
k = 2 : 

'''

import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[[0, -1]*N for _ in range(N)] for _ in range(N)]

# 알파벳의 종류와 개수에 상관없이, k=0이 나오도록 하는 경우(순서 배열)는 항상 만들 수 있다.
def dfs(numA, numB, numC, k):
    if numA == 0 and numB == 0 and numC == 0:
        if k == 0 :
            return ''
        # k < 0이면 마찬가지로 답이 성립이 안하는 것이므로 -1 리턴해야 한다?
        else:
            return -1
    '''
    numA, numB, numC에 대해 항상 k는 존재한다. 최대의 k를 dp에 저장해야 한다.
    '''
    if k == 0:
        return 'C'*numC + 'B'*numB + 'A'*numA
    
    a, b, c = numA, numB, numC
    next_k = k
    
    for last_char in ['A', 'B', 'C']:
        if last_char == 'A':
            a -= 1
        elif last_char == 'B':
            b -= 1
            next_k -= numA
        else:
            c -= 1
            next_k -= numA+numB
    
        # dp[a][b][c][0] <- 가장 큰 k 값을 채우는 게 목표.
        # 현재 dp 값이 next_k보다 크면 굳이 업데이트 할 필요가 없다(아래까지).
        if dp[a][b][c][0] > next_k:
            # continue를 해야 하나? 잘 모르겠다.
            res = -1
        elif dp[a][b][c][0] == next_k:
            res = dp[a][b][c][1]
        else:
            res = dfs(a, b, c, next_k)
            
        # dp[a][b][c][0] > next_k 이면, dp[numA][numB][numC]도 k보다 클 것이고 따라서 업데이트하지 말아야?
        if res != -1:
            if dp[numA][numB][numC][0] == -1 or k > dp[numA][numB][numC][0]:
                dp[numA][numB][numC][0] = k
                dp[numA][numB][numC][1] = res + last_char
    
    return dp[numA][numB][numC][1]



for comb in combinations(range(N), r=2):
    a1, a2 = comb
    # N개의 알파벳으로 이루어진 문자열에서 nA, nB, nC는 각각 알파벳 A,B,C의 개수를 의미
    # nA + nB + nC 는 항상 N이다
    nA, nB, nC = a1, a2-a1-1, N-1-a2
    
    dfs(nA, nB, nC, k)
    

    '''
    dp[0][1][2] -> nA = 0, nB = 1, nC = 2일 때 어떤 string
    따라서
    dp 초기화는
    dp = [[['']*N for _ in range(N)] for _ in range(N)]
    [ [['', '', ''], ['', '', ''], ['', '', '']],
      [['', '', ''], ['', '', ''], ['', '', '']],
      [['', '', ''], ['', '', ''], ['', '', '']]]
    '''


    
    # 이전 알파벳이 A이었다.
    # dp[i-1][0] == 3이라고 하자. 즉, i-1에서 A를 골랐을 때 k=3이다.
    '''
    예시) ABCA
    그 말은, 여기에 A를 붙이면(ABCA+A) 똑같이 여전하다는 뜻
    '''
    
    '''
    dp[i-1][0] = [num_A=2, num_B=1, num_C=1, k=3]
    ABCAB -> B를 붙이면 K = k + num_A = 5, 새로운 num_A = num_A
    
    
    3번째 아이디어:
    계속 K를 증가시키는 방향으로 재귀함수를 실행하고, 그 와중에도 dp에 저장
    만약에 중간에 K에 다다르면 길이가 N이 될 때까지는 계속 A를 붙여나가면 되니까
    
    BACC가 있다고 하자. -> k = 4 (앞에서부터 차례로 카운트)
    여기에 앞에 B를 붙이면 -> k += 2
    여기에 뒤에 B를 붙이면 -> k += 1
    그래서 앞, 혹은 뒤에 추가되는 문자 입장에서는 기존 문자열 알파벳 순서가 중요하지 않다. 어떤 알파벳이 몇개 있느냐가 중요할 뿐.
    그래서 k를 더해준다.
    그럼 알파벳의 개수로 기준을 세울까? 
    N개의 알파벳(종류에 상관없이)이 이미 있다고 가정하자. 순서는 모른다. 
    '''
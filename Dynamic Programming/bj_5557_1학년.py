import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
LIMIT = 20

# dp[n][k] = n번째 중간까지 합산(덧셈, 뺄셈)한 결과에서 k가 등장한 횟수
dp = [[0]*(LIMIT+1) for _ in range(N-1)]
dp[0][numbers[0]] = 1


for i in range(1, N-1):
    for j in range(LIMIT+1):
        if dp[i-1][j] > 0:
            plus  = j + numbers[i]
            minus = j - numbers[i]
            if 0 <= plus <= LIMIT:
                dp[i][plus] += dp[i-1][j]
            if 0 <= minus <= LIMIT:
                dp[i][minus] += dp[i-1][j]

print(dp[-1][numbers[-1]])
        
    
'''
예를 들어 N = 3, numbers = 8 3 5 로 주어졌다고 해보자.
dp[0]은 numbers의 첫번째 숫자 정보를 그대로 저장
dp[1]은 첫번째(최초) 덧셈(혹은 뺄셈) 결과를 저장
따라서 N=3(N의 최소값)이면 dp 배열의 길이는 최대 2
그럼 dp[0] -> 5, 11
len(dp[0]) = 21
dp[0][0] = False, dp[0][1] = False, dp[0][2] = False... dp[0][5] = True, ..., dp[0][11] = True...

dp[0][8] = True
dp
'''
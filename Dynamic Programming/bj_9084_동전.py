import sys
input = sys.stdin.readline

def solution(N, coins, target):
    dp = [[0]*(target+1) for _ in range(N)]
    
    for t in range(coins[0], target+1, coins[0]):
        dp[0][t] = 1
    
    for i in range(1, N):
        cur_val = coins[i]
        if cur_val <= target:
            dp[i][cur_val] += 1
        
        for j in range(target+1):
            # 동전 가치가 2,5,10이라고 해보자. 
            # 5일 때는, dp[1][0] ~ dp[1][4]까지는 동전 5를 쓸 수 없으므로 모두 dp[0]에서 값을 그대로 가져와야 한다.
            if j < cur_val:
                dp[i][j] = dp[i-1][j]
            else:
                # 현재 동전을 쓰지 않고 j를 만드는 방법과
                dp[i][j] += dp[i-1][j]
                # 현재 동전을 꼭 써서 j를 만드는 방법 이 둘을 합한다.
                dp[i][j] += dp[i][j-cur_val]
    
    return dp[-1][-1]


'''
2 5 10
target = 30

dp[0][2], dp[0][4], ... dp[0][30] = 1
dp[1][5], dp[1][7] -> dp[1][2] vs. dp[0][2] ?
dp[1][12]는? -> dp[0][12] 또는 dp[1][7]을 그대로 가져오거나, dp[0][7]을 그대로 가져오거나
근데 여기선 dp[1][7]가 이미 dp[0][7]을 포함하기 때문에, dp[1][7]만 신경쓰면 될 듯
dp[2][10] = 2로만 더한 것 + 5로 포함해서 더한 것 + 10 포함해서 더한 것
dp[1][7] = 1 (2 + 5)
dp[0][7] = 0

'''

# 테스트 케이스의 개수
T = int(input())
for _ in range(T):
    # 동전의 개수
    num_coins = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    print(solution(num_coins, coins, target))

'''
2 * 15
2 * 10 + 5 * 2
2 * 5 + 5 * 4
5 * 6
10 * 1 + 20을 만드는 방법 수 -> 2가지 -> 3가지
10 * 2 + 10을 만드는 방법 수 -> 2가지
10 * 3 -> 1가지
총 10가지
'''
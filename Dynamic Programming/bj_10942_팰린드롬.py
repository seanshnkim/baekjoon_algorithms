import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = [[0]*N for _ in range(N)]
for n in range(N):
    dp[n][n] = 1


# 짝수 길이의 palindrome
for i in range(N-1):
    if numbers[i] == numbers[i+1]:
        dp[i][i+1] = 1
        j = 1
        while i-j >= 0 and i+1+j < N:
            if numbers[i-j] == numbers[i+1+j]:
                dp[i-j][i+1+j] = 1
                j += 1
            # 이게 핵심. 더 이상 palindrome이 아니면 중단한다.
            else:
                break

# 홀수 길이의 palindrome
for i in range(1, N-1):
    if numbers[i-1] == numbers[i+1]:
        dp[i-1][i+1] = 1
        j = 1
        while i-1-j >= 0 and i+1+j < N:
            if numbers[i-1-j] == numbers[i+1+j]:
                dp[i-1-j][i+1+j] = 1
                j += 1
            else:
                break


n_quest = int(input())
for _ in range(n_quest):
    S, E = map(int, input().split())
    S -= 1
    E -= 1
    print(dp[S][E])

'''
1 2 1 3 1 2 1
1 -> T
1 2 -> F
1 2 1 -> T
1 2 1 3 ->
'''

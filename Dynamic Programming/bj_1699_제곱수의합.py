import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]
dp[1] = 1

for i in range(2, N+1):
    if i**2 <= N:
        dp[i**2] = 1
    if dp[i] == 1:
        continue
    for j in range(i-1, 0, -1):
        if dp[j] == 1:
            #FIXME - 반례) 82009. 정답은 2
            '''sqrt(82009)는 286.372이나, 82009는 286^2 + x^2로 쪼개지지 않는다.
            즉, 어떤 수를 제곱수의 합으로 나타내고자 할 때, 그 수보다 작되 가장 큰 제곱수가 포함된다고 해서
            가장 적은 개수의 제곱수 합으로 언제나 나타낼 수 있는 건 아니다(직관적으로 그런 것 같지만 그러리라는 보장이 없다)
            '''
            dp[i] = dp[j] + dp[i-j]
            break

print(dp[N])
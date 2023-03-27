def dynamic_programming(n, k):
    ans = ""

    dp[1][0][0][0] = "A"
    dp[0][1][0][0] = "B"
    dp[0][0][1][0] = "C"

    for a in range(n):
        for b in range(n):
            for c in range(n):
                for t in range(k+1):
                    if a+b+c > n:
                        continue
                    if len(dp[a][b][c][k]) == n:
                        ans = dp[a][b][c][k]
                        return ans

                    if dp[a][b][c][t] != "":
                        if t+a+b <= k:
                            dp[a+1][b][c][t] = dp[a][b][c][t] + "A"
                            dp[a][b+1][c][t+a] = dp[a][b][c][t] + "B"
                            dp[a][b][c+1][t+a+b] = dp[a][b][c][t] + "C"

    return ans


n, k = map(int, input().split())
dp = [[[[ "" for _ in range(k+1)] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

answer = dynamic_programming(n, k)

if answer == "":
    print(-1)
else:
    print(answer)
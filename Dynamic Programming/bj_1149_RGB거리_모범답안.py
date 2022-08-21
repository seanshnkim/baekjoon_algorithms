from sys import stdin

read = lambda: stdin.readline().split()

N = int(input())

costs = []
for _ in range(N):
    costs.append(list(map(int, read())))


DP =[[0]*3 for _ in range(N)]
for i in range(N):
    if i == 0:
        DP[i] = costs[i]
    else:
        DP[i][0] = costs[i][0] + min(DP[i-1][1], DP[i-1][2])
        DP[i][1] = costs[i][1] + min(DP[i-1][0], DP[i-1][2])
        DP[i][2] = costs[i][2] + min(DP[i-1][0], DP[i-1][1])

min_val = min(DP[N-1][0], DP[N-1][1], DP[N-1][2])
print(min_val)
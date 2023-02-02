import time

start = time.time()

n = int(input())
d = [0]*(n+1)
for i in range(1, n+1):
    d[i] = i
    j = 1
    while j*j <= i:
        if d[i] > d[i-j*j]+1:
            d[i] = d[i-j*j]+1
        j += 1
print(d[n])

print(time.time() - start)

'''
import math
n = int(input())
dp = [0 for i in range(n + 1)]
MAX_NUM = 100000
square = [i * i for i in range(1, int(math.sqrt(MAX_NUM))+1 )]
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])
'''
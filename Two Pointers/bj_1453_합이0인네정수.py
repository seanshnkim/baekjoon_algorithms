import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
arrA, arrB, arrC, arrD = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    arrA.append(a)
    arrB.append(b)
    arrC.append(c)
    arrD.append(d)

dict_AB = defaultdict(int)
ans = 0

for i in range(N):
    for j in range(N):
        dict_AB[arrA[i] + arrB[j]] += 1

for i in range(N):
    for j in range(N):
        cur = arrC[i] + arrD[j]
        cur *= -1
        if dict_AB[cur] > 0:
            ans += dict_AB[cur]

print(ans)
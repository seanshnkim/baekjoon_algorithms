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
        sum_AB = arrA[i] + arrB[j]
        dict_AB[sum_AB] += 1

for i in range(N):
    for j in range(N):
        sum_CD = arrC[i] + arrD[j]
        sum_CD *= -1
        # cur_cnt = dict_AB[sum_CD]
        # if cur_cnt > 0:
        #     ans += cur_cnt
        if sum_CD in dict_AB.keys():
            ans += dict_AB[sum_CD]

print(ans)
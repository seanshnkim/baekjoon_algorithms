# 2022-06-25(June 25th, 2022), Sehyun Kim

##### 시간 초과 코드 #####
# numInput = int(input())
# a = set()

# for n in range(numInput):
#     a.add(int(input()))

# print(i in sorted(a), sep = '\n')

import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
l_sorted = sorted(l)
for i in l_sorted:
    sys.stdout.write(str(i)+'\n')


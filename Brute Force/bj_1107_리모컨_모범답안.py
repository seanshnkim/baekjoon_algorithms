import sys
import math
from itertools import product

targ = int(sys.stdin.readline())
num_unavail = int(sys.stdin.readline())

unavail = []
if num_unavail > 0:
    unavail = list(map(int, (sys.stdin.readline().split())))


def is_available(num):
    digit = 0
    if num == 0:
        if 0 in unavail:
            return 0
        else:
            # if 0 is available, since 0 is unit(1) digit
            return 1
    else:
        while num > 0:
            if (num % 10) in unavail:
                return 0
            digit += 1
            num = num // 10
        return digit


answer = abs(targ - 100)

for num in range(1000000):
    digit = is_available(num)
    
    if digit > 0:
        answer = min(answer, abs(targ - num) + digit)

print(answer)
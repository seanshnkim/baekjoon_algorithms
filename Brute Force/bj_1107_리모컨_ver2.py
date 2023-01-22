import sys
import math
from itertools import product

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
availables = set(i for i in range(10))

if M > 0:
    unavailables = set(map(int, (sys.stdin.readline().split())))
    availables = availables - unavailables

digit = int(math.log10(N)) + 1
sample = 0
min_diff = abs(N - 100)

for sample in product(list(availables), repeat=digit):
    if min_diff == 0:
        break
    sample_num = 0
    for d in reversed(range(digit)):
        sample_num += sample[d] * 10**d
    min_diff = min(min_diff, abs(N - sample_num))

#FIXME - 여기서도 실수가 발생
answer = digit + min_diff
if abs(N-100) < answer:
    answer = abs(N-100)
    
print(answer)
    
    
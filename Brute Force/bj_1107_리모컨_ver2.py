import sys
import math
from itertools import product

targ = int(sys.stdin.readline())
num_unavail = int(sys.stdin.readline())
availables = set(i for i in range(10))

if num_unavail > 0:
    unavailables = set(map(int, (sys.stdin.readline().split())))
    availables = availables - unavailables

# if targ == 0, digit = 1
if targ == 0:
    digit = 1
else:
    digit = int(math.log10(targ)) + 1

sample = 0
min_diff = abs(targ - 100)

possible_nums = []
for d in range(1, digit+2):
    possible_nums.extend(list(product(list(availables), repeat=d)))
    
for sample in possible_nums:
    if min_diff == 0:
        break
    digit = len(sample)
    sample_num = sum(sample[i]*10**(digit-i-1) for i in range(digit))
    min_diff = min(min_diff, abs(targ - sample_num) + digit)
    
print(min_diff)

'''
Counterexample 1:
99999
9
0 2 3 4 5 6 7 8 9
expected(answer): 11118
output(false): 88893

--> if the number of digits of targ is D, it can start from D+1 digit number
(만약 목표 targ 값이 D 자릿수라면, D+1 자릿수부터 시작해서 1씩 빼면서 최소 차이값을
구할 수 있다)
'''


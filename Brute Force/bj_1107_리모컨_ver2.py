import sys
import math
from itertools import product

targ = int(sys.stdin.readline())
num_unavail = int(sys.stdin.readline())
availables = set(i for i in range(10))

if num_unavail > 0:
    unavailables = set(map(int, (sys.stdin.readline().split())))
    availables = availables - unavailables
availables = sorted(list(availables))

# if targ == 0, digit = 1
digit = int(math.log10(targ))+1 if targ > 1 else 1
min_diff = abs(targ - 100)

# First, search among D digit numbers
# 만약 주어진 targ 숫자가 D자리면 D자릿수의 숫자부터 하나씩 대입해본다.
for sample in product(availables, repeat=digit):
    if min_diff == 0:
        break
    sample_num = sum(sample[i]*10**(digit-i-1) for i in range(digit))
    curr_diff = abs(targ - sample_num) + digit
    min_diff = min(min_diff, curr_diff)

if availables:
    # D-1 자릿수의 숫자를 테스트
    if digit > 1:
        max_low_d = sum(availables[-1]*10**(digit-i-2) for i in range(digit-1))
        min_diff = min(min_diff, abs(targ - max_low_d) + digit-1)
    
    # D+1 자릿수의 숫자를 테스트
    if availables[0] == 0 and len(availables) > 1:
        smallest_d = availables[1]
    else:
        smallest_d = availables[0]
    
    min_great_d = sum(smallest_d*10**(digit-i) for i in range(digit+1))
    min_diff = min(min_diff, abs(min_great_d - targ) + digit+1) 

    
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


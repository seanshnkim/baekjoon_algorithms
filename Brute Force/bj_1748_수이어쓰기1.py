import sys
import math

N = int(sys.stdin.readline())

digit = int(math.log10(N)) + 1
length = 0

if digit == 1:
    length = N
else:
    length += (N - 10**(digit-1) + 1) * digit
    digit -= 1
    while digit > 0:
        length += 9*(10**(digit-1)) * digit
        digit -= 1

print(length)
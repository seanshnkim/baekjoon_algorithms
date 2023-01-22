import sys
import math

def solution(NUM1, NUM2, x, y):
    i = 0
    if NUM1 < NUM2:
        while i < NUM2:
            cnt = NUM1 * i + x
            if ((NUM1 * i) % NUM2 + x) % NUM2 == y:
                return cnt
            i += 1
    else:
        while i < NUM1:
            cnt = NUM2 * i + y
            if ((NUM2 * i) % (NUM1) + y) % NUM1 == x:
                return cnt
            i += 1
            
    return -1
    

num_test_input = int(sys.stdin.readline())

for t in range(num_test_input):
    NUM1, NUM2, x, y = map(int, sys.stdin.readline().split())
    print(solution(NUM1, NUM2, x, y))
    
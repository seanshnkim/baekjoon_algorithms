import sys
import math

num_test_input = int(sys.stdin.readline())

for t in range(num_test_input):
    NUM1, NUM2, x, y = map(int, sys.stdin.readline().split())
    
    cnt = 1
    n1 = n2 = 1
    while not (n1 == NUM1 and n2 == NUM2):
        if n1 == x and n2 == y:
            break
        n1 += 1
        n2 += 1
        if n1 > NUM1:
            n1 = 1
        if n2 > NUM2:
            n2 = 1
        cnt += 1
    
    if (x,y) != (NUM1, NUM2) and cnt == math.lcm(NUM1, NUM2):
        print(-1)
    else:
        print(cnt)
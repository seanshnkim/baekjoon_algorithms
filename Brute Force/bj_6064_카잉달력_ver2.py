import sys
import math

# 이렇게 풀 경우 x 또는 y가 NUM1, NUM2와 같을 때 나머지를 반영하지 못한다.
def solution(NUM1, NUM2, x, y):
    i = 0
    while i < NUM2:
        cnt = NUM1 * i + x
        if cnt % NUM2 == y:
            return cnt
        i += 1
    return -1
        

num_test_input = int(sys.stdin.readline())

for t in range(num_test_input):
    NUM1, NUM2, x, y = map(int, sys.stdin.readline().split())
    print(solution(NUM1, NUM2, x, y))
    
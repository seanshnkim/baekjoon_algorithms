import sys

# x,y를 -1 하지 않으면 x == NUM1, y == NUM2와 같은 입력이 주어졌을 때,
# x == NUM1 or y == NUM2 --> (cnt % NUM1) == (cnt % NUM2) == 0된다
# x 또는 y이어야 하므로 아래 공식이 성립 X
def solution(NUM1, NUM2, x, y):
    x -= 1
    y -= 1
    i = 0
    while i < NUM2:
        cnt = NUM1 * i + x
        if cnt % NUM2 == y:
            return cnt + 1
        i += 1
    return -1
        

num_test_input = int(sys.stdin.readline())

for t in range(num_test_input):
    NUM1, NUM2, x, y = map(int, sys.stdin.readline().split())
    print(solution(NUM1, NUM2, x, y))
    
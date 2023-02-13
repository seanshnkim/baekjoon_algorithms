import sys
input = sys.stdin.readline


def is_VPS(input_str):
    stack = [s for s in input_str]
    cnt = 0
    while stack:
        top = stack.pop()
        if top == ')':
            cnt += 1
        elif top == '(':
            cnt -= 1
        # 괄호가 거꾸로, )( 이런 식으로 나온 경우
        if cnt < 0:
            return False
            
    return cnt == 0


N = int(input())
for _ in range(N):
    if is_VPS(input()):
        print("YES")
    else:
        print("NO")
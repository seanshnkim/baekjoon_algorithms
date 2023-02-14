import sys
input = sys.stdin.readline

input_str = input().rstrip('\n')
N = int(input())
commands = [input().rstrip('\n') for _ in range(N)]

stack_left = [s for s in input_str]
stack_right = []

for com in commands:
    # L, D, B, P $
    if com == "L":
        if stack_left:
        #NOTE - IndexError: pop from empty list
            stack_right.append(stack_left.pop())
    elif com == "D":
        if stack_right:
            stack_left.append(stack_right.pop())
    elif com == "B":
        if stack_left:
            stack_left.pop()
    else:
        insert_char = com.split()[1]
        stack_left.append(insert_char)

answer = ''.join(stack_left) + ''.join(stack_right[::-1])
print(answer)
import sys
input = sys.stdin.readline

stack = []

# push, pop, size, empty, top
length = 0
N = int(input())

for _ in range(N):
    commands = input().split()
    if commands[0] == "push":
        stack.append(commands[1])
        length += 1
    elif commands[0] == "pop":
        if length > 0:
            print(stack.pop())
            length -= 1
        else:
            print(-1)
    elif commands[0] == "size":
        print(length)
    elif commands[0] == "empty":
        if length > 0:
            print(0)
        else:
            print(1)
    elif commands[0] == "top":
        if length > 0:
            print(stack[-1])
        else:
            print(-1)
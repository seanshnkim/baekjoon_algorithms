import sys

while True:
    input_str = sys.stdin.readline().rstrip('\n')
    if input_str == '0':
        break
    elif input_str == input_str[::-1]:
        print("yes")
    else:
        print("no")
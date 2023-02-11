import sys
input = sys.stdin.readline

input_str = input().rstrip('\n')
explode = input().rstrip('\n')
len_input = len(input_str)
len_exp = len(explode)

output = []
stack = []

def is_consecutive(output, stack, c):
    if not (len(output) >=2 and stack):
        return False
    else:
        return output[-2:] == [stack[-1]] + [c]
    

if len_exp == 1:
    print(''.join([c for c in input_str if c != explode]))
else:
    for i in range(len_input):
        curr = input_str[i]
        output.append(curr)
        
        if curr == explode[0]:
            stack.append(curr)
        elif is_consecutive(output, stack, curr):
            stack.append(curr)
            if curr == explode[-1]:
                for _ in range(len_exp):
                    stack.pop()
                    output.pop()
    
    if not output:
        print("FRULA")
    else:
        print(''.join(output))
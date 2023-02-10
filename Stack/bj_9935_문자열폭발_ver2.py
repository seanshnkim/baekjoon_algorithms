import sys
input = sys.stdin.readline

input_str = input().rstrip('\n')
explode = input().rstrip('\n')
len_input = len(input_str)
len_exp = len(explode)

output_str = ''
stack = ''

def is_consecutive(output, stack, c):
    if not (len(output_str) >=2 and stack):
        return False
    else:
        #REVIEW - 파이썬 리스트 인덱싱 복습해야 할 듯
        # return output[:-2] == stack[-1] + c
        return output[-2:] == stack[-1] +c
    

if len_exp == 1:
    print(''.join([c for c in input_str if c != explode]))
else:
    for i in range(len_input):
        curr = input_str[i]
        output_str += curr
        
        if curr == explode[0]:
            stack += curr
        elif is_consecutive(output_str, stack, curr):
            stack += curr
            if curr == explode[-1]:
                stack = stack[:-len_exp]
                output_str = output_str[:-len_exp]
    
    if not output_str:
        print("FRULA")
    else:
        print(''.join(output_str))
import sys
input = sys.stdin.readline
from collections import deque

infix = input().rstrip('\n')
len_infix = len(infix)

def is_operator(s):
    if s == '+' or s == '-' or s == '*' or s == '/':
        return True
    else:
        return False


def read_equation(start):
    if start == len_infix-1:
        return ''
    
    i = start
    left = deque()
    right = deque()
    op = deque()
    
    # Search left
    if infix[i] == '(':
        p = []
        while infix[i] != ')':
            i += 1
            p.append(infix[i])
        small_eq = read_equation(p)
        left.append(small_eq)
        # 괄호는 안 넣어도 되니까
        i += 1
        
    elif i < len_infix:
        while not is_operator(infix[i]):
            left.append(infix[i])
            i += 1
        
        if i < len_infix:
            op.append(infix[i])
            i += 1
            
        if i < len_infix:
            right.append(read_equation(i))
    
    answer = []
    while left or right or op:
        if left:
            answer.append(left.popleft())
        if right:
            answer.append(right.popleft())
        if op:
            answer.append(op.popleft())
    
    return answer


print(''.join(read_equation(0)))
            # if not left:
            #     left.append(small_eq)
            # else:
            #     right.append(small_eq)
                
        # elif i < len_eq and is_operator(equation[i]):
        #     op.append(equation[i])
        #     i += 1
            
        # elif i < len_eq and not is_operator(equation[i]):
        #     if not left:
        #         left.append()
    


# def convert2postfix(equation):
#     eq_len = len(equation)
#     i = 0
#     operators = []
#     operands = []
#     while i < eq_len:
#         if equation[i] == '(':
#             small_equation = []
#             while equation[i] != ')':
#                 i += 1
#                 small_equation.append(equation[i])
#             res = convert2postfix(small_equation)
#             operands.append(res)
        
#         elif i < eq_len and is_operator(equation[i]):
#             operators.append(equation[i])
#             i += 1
#         elif i < eq_len:
#             operands.append(equation[i])
#             i += 1
    
#     return operands + 
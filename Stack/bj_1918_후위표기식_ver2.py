import sys
input = sys.stdin.readline

infix_str = input().rstrip('\n')
answer = ''
stack = []


# def is_alphabet(c):
#     if  c != '+' and c != '-' and c != '*' \
#     and c != '/' and c != '(' and c != ')':
#         return True
#     else:
#         return False


def priority(c):
    if c == '+' or c == '-':
        return 0 
    elif c == '*' or c == '/':
        return 1
    elif c == '(' or c == ')':
        return 2
    else:
        return -1
    

for c in infix_str:
    # if is_alphabet(c):
    if priority(c) == -1:
        answer += c
        
    elif priority(c) == 0:
        while stack and priority(stack[-1]) < 2:
            answer += stack.pop()
        stack.append(c)
    
    elif priority(c) == 1:
        while stack and priority(stack[-1]) == 1:
            answer += stack.pop()
        stack.append(c)
    
    elif priority(c) == 2:
        if c == '(':
            stack.append(c)
        else:
            while stack and priority(stack[-1]) < 2:
                answer += stack.pop()
            # 그 다음에 '('를 없애줘야 함. 현재 글자가 )이라면, 반드시 그 이전에
            # '('가 stack에 한 개 이상 담겨 있다는 뜻이므로 len(stack) >= 1이다.
            # 따라서, while문을 break하고 난 뒤에는 (stack and stack[-1] == '(' ) == True이다.
            stack.pop()

while stack:
    answer += stack.pop()

print(answer)
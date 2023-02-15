text = input()
answer = ''
stack = [] # 연산자 관리용

for t in text :
    if t.isalpha() :
        answer += t
    else :
        if t == '(' :
            stack.append(t)
        elif t == '*' or t == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                answer += stack.pop()
            stack.append(t)
        elif t == '+' or t == '-' :
            while stack and stack[-1] != '(' :
                answer += stack.pop()
            stack.append(t)
        elif t == ')' :
            while stack and stack[-1] != '(' :
                answer += stack.pop()
            stack.pop() # '('를 빼는 작업

while stack :
    answer += stack.pop()

print(answer)
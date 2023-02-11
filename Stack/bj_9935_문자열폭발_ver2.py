import sys
input = sys.stdin.readline

input_str = input().rstrip('\n')
explode = input().rstrip('\n')
len_input = len(input_str)
len_exp = len(explode)

output = []
stack = []

ans = []
if len_exp == 1:
    ans = [c for c in input_str if c != explode]
else:
    for i in range(len_input):
        curr = input_str[i]
        output.append(curr)
        
        # FIXME: 반례: explode 문자열이 'abab'인 경우
        # if curr == explode[0]:
        if curr == explode[0]:
            stack.append((curr, 0) )
        elif stack:
            stack.append((curr, stack[-1][1]+1) )
            #FIXME - 반례: input_str이 ababab, explode 문자열이 'abab'인 경우
            #REVIEW - 폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.
            # -> 그럼 모두 서로 다른 문자로 이루어져 있다는 뜻이 아니었나?
            # if curr == explode[-1]:
            if curr == explode[-1] and stack[-1][1] == len_exp-1:
                # stack = stack[:-len_exp]
                # output_str = output_str[:-len_exp]
                for _ in range(len_exp):
                    stack.pop()
                    output.pop()
    ans = output
    
    
if not ans:
    print("FRULA")
else:
    print(''.join(ans))
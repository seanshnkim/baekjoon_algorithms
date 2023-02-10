import sys
input = sys.stdin.readline

input_str = input().rstrip('\n')
explode = input().rstrip('\n')
len_exp = len(explode)

output_idx = []
stack = []

if len_exp == 1:
    print(''.join([c for c in input_str if c != explode]))
else:
    # explode 문자열이 모두 서로 다른 문자로만 이루어져있어야 다음 코드가 가능하다.
    for i in range(len(input_str)):
        output_idx.append(i)
        if input_str[i] == explode[0]:
            stack.append(0)
            
        # FIXME: input_str[i-1]이 아니라 output_str -> 문제 사전 분석이 그래서 중요하다
        # elif stack and input_str[i-1] == explode[stack[-1]] \
        elif stack and input_str[output_idx[-1]] == explode[stack[-1]] \
            and input_str[i] == explode[stack[-1]+1]:
            stack.append(stack[-1]+1)
            
            if stack[-1] == len_exp-1:
                stack = stack[:(len(stack) - len_exp)]
                # FIXME - output_idx[:(i+1-len_exp)] -> output_idx 배열의 길이는
                # 항상 i+1인 게 아니다.
                # output_idx = output_idx[:(i+1-len_exp)]
                output_idx = output_idx[:(len(output_idx)-len_exp)]

print(''.join(input_str[c] for c in output_idx))
import sys
input = sys.stdin.readline

input_str = input().rstrip('\n')
len_input = len(input_str)

i = 0
output_str = ''

while i < len_input:
    if input_str[i] == '<':
        tag = ''
        while input_str[i] != '>':
            tag += input_str[i]
            i += 1
        tag += input_str[i]
        i += 1
        output_str += tag
    else:
        word = ''
        # while input_str[i] != ' ' 만 걸면, 해당 단어가 문자열의 마지막 부분일 때를 포함하지 못함
        # while input_str[i] != ' ' and i < len_input:
        # 또는 또다른 태그의 시작이 오면 중단
        while i < len_input and input_str[i] != ' ' and input_str[i] != '<':
            word += input_str[i]
            i += 1
        output_str += word[::-1]
        if i < len_input and input_str[i] == ' ':
            output_str += ' '
            i += 1

print(output_str)
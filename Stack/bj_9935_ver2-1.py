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
        
        if curr == explode[0]:
            stack.append((curr, 0) )
        
        # stack에 원소가 있다는 건 len(output) >= 2 와 동치
        elif stack:
            if output[-2] == stack[-1][0] and curr == explode[stack[-1][1]+1]:
                stack.append((curr, stack[-1][1]+1) )
                if curr == explode[-1]:
                    for _ in range(len_exp):
                        stack.pop()
                        output.pop()
    ans = output
    
if not ans:
    print("FRULA")
else:
    print(''.join(ans))
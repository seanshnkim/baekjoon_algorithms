import sys
input = sys.stdin.readline

input_str = input().rstrip('\n')
explode = input().rstrip('\n')
len_input = len(input_str)
len_exp = len(explode)

stack = []
erased = [False]*len_input

ans = []
if len_exp == 1:
    ans = [c for c in input_str if c != explode]
else:
    for i in range(len_input):
        curr = input_str[i]
        
        if curr == explode[0]:
            stack.append((i, 0))
        else:
            if stack:
                first = stack[-1]
                if input_str[i] == explode[first[1]+1]:
                    stack.append((i, first[1]+1) )
                    
                    if first[1]+1 == len_exp-1:
                        for _ in range(len_exp):
                            f = stack.pop()
                            erased[f[0]] = True
                            
                # else:
                #     while stack:
                #         stack.pop()
                else:
                    stack.clear()
                        
    output = [input_str[i] for i in range(len_input) if not erased[i]]
    ans = output
    
if not ans:
    print("FRULA")
else:
    print(''.join(ans))
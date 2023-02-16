def solution(number, k):
    stack = [number[0]]
    cnt = 0
    for i in range(1, len(number)):
        # if cnt == k:
        #     break
        while stack and stack[-1] < number[i] and cnt < k:
            stack.pop()
            cnt += 1
        stack.append(number[i])
        
    return ''.join(stack)

# print(solution("1231234", 3))
print(solution("4177252841", 4))
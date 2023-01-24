import sys

n_signs = int(sys.stdin.readline())
signs = list(sys.stdin.readline().split())


def solution(idx, num_list):
    if idx == n_signs:
        num = sum(num_list[i]*10**(n_signs-i) for i in range(n_signs+1))
        return num, num
    
    min_num = 10**(n_signs+1) - 1
    max_num = -1
    
    # 처음 num_list = [] -> empty list이면 i를 default 값으로 더해줘야
    if not num_list:
        for i in range(10):
            num_list += [i]
            ## something solution ##!SECTION
            for i in range(10):
                if i in num_list:
                    continue
                if  (signs[idx] == '>' and num_list[-1] > i) or \
                    (signs[idx] == '<' and num_list[-1] < i):
                        min_res, max_res = solution(idx+1, num_list+[i])
                        if min_num == 10**(n_signs+1)-1 or max_num == -1:
                            if min_res != -1 and max_res != -1:
                                min_num = min(min_num, min_res)
                                max_num = max(max_num, max_res)
            num_list.pop()
            
        return min_num, max_num
    
    
    for i in range(10):
        if i in num_list:
            continue
        if  (signs[idx] == '>' and num_list[-1] > i) or \
            (signs[idx] == '<' and num_list[-1] < i):
            min_res, max_res = solution(idx+1, num_list+[i])
            if min_num == 10**(n_signs+1)-1 or max_num == -1:
                if min_res != -1 and max_res != -1:
                    min_num = min(min_num, min_res)
                    max_num = max(max_num, max_res)
    
    # 항상 불가능한 답이 나오는 경우를 생각해야
    return min_num, max_num
    
    
print(solution(0, []))

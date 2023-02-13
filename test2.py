# digit = 0

def solution(numbers):
    numbers_str = [str(n) for n in numbers]
    numbers_str.sort(key=lambda x: x*3, reverse=True)

    # 만약 0이 여러 개 나오는 경우라면
    if numbers[0] == '0':
        return '0'
    else:
        return ''.join(numbers_str)
    # return str(int(''.join(numbers_str)))

print(solution([0,0,0,0]))
    # table = [[] for _ in range(10)]
    # answer = ''
    # global digit

    # for n in numbers:
    #     idx = int(str(n)[0])
    #     if len(str(n)) > digit and digit > 0:
    #         idx = int(str(n)[digit])

    #     table[idx].append(n)

    # for i in range(9, -1, -1):
    #     if len(table[i]) == 0:
    #         continue
    #     elif len(table[i]) == 1:
    #         # ans_idx.append() 
    #         answer += str(table[i][0])
    #     else:
    #         digit += 1
    #         answer += solution(table[i])

    # return answer
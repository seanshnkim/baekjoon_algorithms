digit = 0

def solution(numbers):
    table = [[] for _ in range(10)]
    answer = ''
    global digit

    for n in numbers:
        idx = int(str(n)[0])
        if len(str(n)) > digit and digit > 0:
            idx = int(str(n)[digit])

        table[idx].append(n)

    for i in range(9, -1, -1):
        if len(table[i]) == 0:
            continue
        elif len(table[i]) == 1:
            # ans_idx.append() 
            answer += str(table[i][0])
        else:
            digit += 1
            answer += solution(table[i])

    return answer

print(solution([3,30,34,5,9]))
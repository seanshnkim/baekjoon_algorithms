def solution(numbers, target):
    if len(numbers) == 2:
        if (numbers[0] + numbers[1]) == target:
            return 1
        elif (numbers[0] - numbers[1]) == target:
            return 1
        elif (numbers[1] - numbers[0]) == target:
            return 1
        elif -(numbers[0] + numbers[1]) == target:
            return 1
        elif numbers[1] == target:
            return 1
        else:
            return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])

# base case를 더 간단하게 고침
# recursion을 활용, 논리는 BFS(breadth first search)
def solution2(numbers, target):
    if len(numbers) == 1:
        if numbers[0] == target or (-numbers[0]) == target:
            print('target:', target)
            return 1
        else:
            print('target:', target)
            return 0
    else:
        print('target:', target)
        return solution2(numbers[1:], target - numbers[0]) + solution2(numbers[1:], target + numbers[0])

test_case1 = [1,1,1,1,1]
test_case2 = [4,1,2,1]


# print(solution(test_case1, 3))
# print(solution(test_case2, 5))

print(solution2(test_case1, 3))
print(solution2(test_case2, 4))

# 다른 사람의 풀이 : best
def solution_best(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbersPt[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# python의 itertools.product과 map을 이용한 풀이
# 예를 들어 numbers = [1,2,3,4,5]이라고 하자.
# 1,2,3,4,5 각 숫자를 더하거나 뺄 수 있는 경우는 2가지(+, -).
# 각 숫자를 더하거나 빼서 연산하는 경우는 따라서 2**5 = 32가지 (이걸 itertools.product로 Cartesian products를 만들어서 구한다)
from itertools import product
def solution_map(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

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
#print(solution2(test_case2, 4))


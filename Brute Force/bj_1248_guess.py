import sys

N = int(sys.stdin.readline())
signs = sys.stdin.readline()
possible_nums = []
sum_list = [[0 for _ in range(N)] for _ in range(N)]

sign_matrix = [['*' for _ in range(N)] for _ in range(N)]
start = 0
# for i in reversed(range(1, N+1)):
for i in range(N):
    sign_matrix[i][i:] = signs[start:start+(N-i)]
    start += (N-i)


def compare(curr_sum, sign):
    if sign == '-' and curr_sum < 0:
        return True
    if sign == '+' and curr_sum > 0:
        return True
    if sign == '0' and curr_sum == 0:
        return True
    return False


def solution(idx, curr_nums):
    if idx == N:
        possible_nums.append(curr_nums)
        return
    
    sign_of_ith = sign_matrix[idx][idx]
    curr_range = range(-10, 11)
    if sign_of_ith == '-':
        curr_range = range(-10, 0)
    elif sign_of_ith == '+':
        curr_range = range(1, 11)
    else:
        curr_range = range(0, 1)
    
    for n in curr_range:
        if idx == 0:
            sum_list[0][0] = n
            solution(idx+1, curr_nums+[n])
        else:
            for i in range(idx):
                sum_up_to_idx = sum_list[i][idx-1] + n
                if compare(sum_up_to_idx, sign_matrix[i][idx]):
                    # update sum_list
                    for j in range(idx+1):
                        sum_list[j][idx] += sum_list[j][idx-1] + n
                    solution(idx+1, curr_nums+[n])
                    # 이렇게 해서 꼭 다시 리셋해주어야 함
                    for j in range(idx+1):
                        sum_list[j][idx] -= sum_list[j][idx-1] + n
    return


solution(0, [])
print(possible_nums[0])


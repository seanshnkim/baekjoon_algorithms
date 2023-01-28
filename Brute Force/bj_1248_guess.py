import sys

N = int(sys.stdin.readline())
signs = sys.stdin.readline()
answers = []
# sum_list = [[0 for _ in range(N)] for _ in range(N)]

sign_matrix = [['*' for _ in range(N)] for _ in range(N)]
start = 0
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


def solution(idx, cumul_nums, idx_sums):
    if idx == N:
        answers.append(cumul_nums)
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
            idx_sums = [n]
            solution(idx+1, cumul_nums+[n], idx_sums)
        else:
            possible_nums = []
            new_idx_sums = []
            for i in range(idx):
                if compare(idx_sums[i]+n, sign_matrix[i][idx]):
                    # 아 여기서 AND로 솎아냈어야 했는데 그냥 OR로 처리했다.
                    possible_nums.append(n)
                    
    if idx != 0:
        new_idx_sums.append(idx_sums[i]+n)
        new_idx_sums.append(n)
    
        for n in possible_nums:
            for i in range(idx):
                new_idx_sums.append(idx_sums[i]+n)
            new_idx_sums.append(n)
            
            solution(idx+1, cumul_nums+[n], new_idx_sums)
    
    return


solution(0, [], [])
print(possible_nums[0])


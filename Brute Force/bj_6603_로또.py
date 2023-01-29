import sys

def solution(curr_idx):
    if curr_idx == 5:
        idx_in_input = nums.index(seq[curr_idx])
        while (N-1 - idx_in_input) >= (5-curr_idx) and idx_in_input < N-1:
            print(' '.join(map(str, seq)))
            seq[curr_idx] = nums[idx_in_input+1]
            idx_in_input = nums.index(seq[curr_idx])
        return
    
    idx_in_input = nums.index(seq[curr_idx])
    while (N-1 - idx_in_input) >= (5-curr_idx):
        solution(curr_idx+1)
        seq[curr_idx] = nums[idx_in_input+1]
        idx_in_input = nums.index(seq[curr_idx])
    
    return


while True:
    input = sys.stdin.readline().split()
    if input == ['0']:
        break
    test_input = list(map(int, input))
    N, nums = test_input[0], test_input[1:]
    seq = nums[:6]
        
    solution(0)


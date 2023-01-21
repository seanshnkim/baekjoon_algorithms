import sys
from typing import List

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# 실패: List(candidates) index out of range
def solution_1(nums: List, S):
    nums_sorted = sorted(nums)
    candidates = []
    cnt = 0
    
    for n in nums_sorted:
        for i in range(len(candidates)):
            new = candidates[i] + n
            if new > S:
                curr_c = candidates[i]
                while curr_c in candidates:
                    candidates.remove(curr_c)
            elif new == S:
                cnt += 1
            candidates.append(new)
        candidates.append(n)


# 이것도 계속 리스트에 insert를 하므로 new = candidates[i] + num 에 변동이 생김
def solution_2(nums: List, S):
    nums_sorted = sorted(nums)
    candidates = []
    cnt = 0
    
    for num in nums_sorted:
        for i in range(len(candidates)):
            new = candidates[i] + num
            
            if new > S:
                candidates = candidates[:i]
                break
            elif new == S:
                cnt += 1
            
            j = 0
            while candidates[j] < new and j < len(candidates):
                j += 1
            candidates.insert(j, new)
        
        if not candidates:
            candidates.append(num)
        else:
            j = 0
            while candidates[j] < new:
                j += 1
                candidates.insert(j, num)
    
    return cnt


'''
나는 nums + candidates[i]가 S보다 커지면 더 이상 nums를 순회할 필요가 없으니
candidates에 수정을 가하려고 했는데 그렇게 하는 게 아닌가?
'''

def solution_3(nums: List, S):
    nums_sorted = sorted(nums)
    candidates = []
    cnt = 0
    
    for num in nums_sorted:
        for i in range(len(candidates)):
            new = candidates[i] + num
            if new > S:
                candidates = candidates[:i]
                candidates.append(new)
                break
            elif new == S:
                cnt += 1
            candidates.append(new)
            ...
        candidates.append(num)
        candidates.sort()
    return cnt


def solution_4(idx, curr_sum):
    global cnt
    
    if idx >= N:
        return

    if curr_sum == S:
        cnt += 1
    
    solution_4(idx+1, curr_sum)
    solution_4(idx+1, curr_sum + nums[idx])
    
    

if __name__ == '__main__':
    N, S = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    solution_3(0, 0)
    
    print(cnt)




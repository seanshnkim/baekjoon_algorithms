import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
numbers = list(map(int, input().split()))
# 실제 부분수열의 조건을 이루지는 않음. 길이만 확인 가능
subseq = [numbers[0]]
len_subseq = 1

for i in range(1, N):
    cur_num = numbers[i]
    
    insert_idx = bisect_left(subseq, cur_num)
    
    if insert_idx == len_subseq:
        subseq.append(cur_num)
        len_subseq += 1
    else:
        subseq[insert_idx] = cur_num

print(len_subseq)
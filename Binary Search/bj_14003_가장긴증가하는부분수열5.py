import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
numbers = list(map(int, input().split()))

pseudo_subseq = [numbers[0]]
len_subseq = 1
indices_subseq = [0]*N

for i in range(1, N):
    cur_num = numbers[i]
    
    insert_idx = bisect_left(pseudo_subseq, cur_num)
    
    if insert_idx == len_subseq:
        pseudo_subseq.append(cur_num)
        len_subseq += 1
    else:
        pseudo_subseq[insert_idx] = cur_num
    
    indices_subseq[i] = insert_idx

print(len_subseq)

subseq = [0]*len_subseq
# 끝에서부터 앞으로 차례로 탐색 -> 최장 증가 부분 수열은 결국 방향성(배열의 앞 -> 뒤)을 가지고 있기 때문
subseq_idx = len_subseq-1
for i in range(N-1, -1, -1):
    if indices_subseq[i] == subseq_idx:
        subseq[subseq_idx] = numbers[i]
        subseq_idx -= 1

print(*subseq)
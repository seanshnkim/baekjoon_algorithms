import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
# FIXME - is_possible = [False]*(max(seq)*N + 1)
# -> 만약 1부터 max(seq)*N까지 모든 자연수를 만드는 게 가능하다면, ValueError가 발생한다.

# 동적으로 배열 크기를 만들지 않고 고정시킨다면?
MAX_NUM = 100000
MAX_LEN = 20
is_possible = [False]*(MAX_NUM*MAX_LEN + 2)

# 아예 고르지 않는 경우는 부분 수열이라 할 수 없다
# for i in range(1<<N):
for i in range(1, 1<<N):
    curr_sum = 0
    for j in range(N):
        if i & (1<<j) != 0:
            curr_sum += seq[j]
    is_possible[curr_sum] = True

# is_possible[0]은 0을 만들 수 있는 여부를 의미, 따라서 1부터 카운팅해야 함.
# idx = 1
# while is_possible[idx]:
#     idx += 1
# print(idx)
is_possible[0] = True
print(is_possible.index(False))

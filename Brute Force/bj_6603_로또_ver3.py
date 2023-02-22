import sys
input = sys.stdin.readline
from itertools import combinations

while True:
    input_list = list(map(int, input().split()))
    if input_list == [0]:
        break
    K = input_list[0]
    nums = input_list[1:]
    
    for comb in combinations(nums, 6):
        print(*comb)
    print()
import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input().split())
nums = map(int, input().split())
add_nums = [9,3,1]
NSIZE = 60

if N == 1:
    print(nums[0] // 9 + 1)
elif N == 2:
    ...
elif N == 3:
    dp = [[[0]*(NSIZE+1) for _ in range(NSIZE+1)] for _ in range(NSIZE+1)]
    
    def solution(x,y,z, case):
        if x > 60 or y > 60 or z > 60:
            return
        
        for i in range(case[0]):
            for j in range(case[1]):
                for k in range(case[2]):
                    if i == j == k == 0:
                        continue
                    if x+i <= 60 and y+j <= 60 and z+k <= 60 and \
                       dp[x+i][y+j][z+k] == 0:
                        dp[x+i][y+j][z+k] = dp[x][y][z] + 1
        
        for perm in permutations([1,3,9]):
            if dp[x+case[0]][y+case[1]][z+case[2]] == 0:
                solution(x+case[0], y+case[1], z+case[2], list(perm))


    for i in range(9):
        for j in range(3):
            for k in range(1):
                dp[i][j][k] = 1
    dp[0][0][0] = 0

    for perm in permutations([1,3,9]):
        solution(9,3,1, list(perm))

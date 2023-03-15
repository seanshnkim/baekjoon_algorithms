import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
if len(nums) < 3:
    nums += [0]*(3-len(nums))

NSIZE = 60
dp = [[[-1]*(NSIZE+1) for _ in range(NSIZE+1)] for _ in range(NSIZE+1)]

def solution(x,y,z):
    # 범위 설정을 2^3 = 8번 일일이 하기 어렵기 때문에 이렇게 하면 코드가 간결해진다.
    # 예를 들어 x, y 2개가 모두 0보다 작아도 결국 재귀함수를 통해 0으로 만들어줄 수 있다.
    if x < 0:
        return solution(0, y, z)
    if y < 0:
        return solution(x, 0, z)
    if z < 0:
        return solution(x, y, 0)
    if x == y == z == 0:
        return 0
    
    answer = dp[x][y][z]
    if answer != -1:
        return answer
    answer = float('inf')
    for perm in permutations([1,3,9]):
        res = solution(x-perm[0], y-perm[1], z-perm[2])
        if answer > res:
            answer = res
    answer += 1
    dp[x][y][z] = answer
    return answer

print(solution(nums[0], nums[1], nums[2]))

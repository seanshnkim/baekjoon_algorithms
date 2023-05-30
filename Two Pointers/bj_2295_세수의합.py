import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
ans = 0

numbers.sort()

def solution():
    for i in range(N-1, 0, -1):
        cur_sum = numbers[i]
        for j in range(i-1, -1, -1):
            cur_sum -= numbers[j]
            if cur_sum < 0:
                cur_sum += numbers[j]
                break
            elif cur_sum > 0:
                for k in range(j, -1, -1):
                    cur_sum -= numbers[k]
                    
                    if cur_sum < 0:
                        cur_sum += numbers[k]
                        break
                    elif cur_sum > 0:
                        for l in range(k, -1, -1):
                            if cur_sum == numbers[l]:
                                return numbers[i]
                    cur_sum += numbers[k]
            
            cur_sum += numbers[j]

print(solution())
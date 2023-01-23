import sys

'''
#FIXME: 1,2,3의 합으로 나타낼 수 있는 경우의 수 -> 순열이 아닌 조합
#NOTE: cnt를 return하게 될 경우 이미 계산한 sum에 대해 cnt를 또다시 더하므로 누적
def solution(cnt, sum, n):
    if sum == n:
        return cnt
    if sum > n:
        return 0
    
    cnt += 1
    # 1을 더한 경우
    return solution(cnt, sum+1, n) + \
           solution(cnt, sum+2, n) + \
           solution(cnt, sum+3, n)
'''

def solution(sum, n):
    if sum == n:
        return 1
    if sum > n:
        return 0

    return solution(sum+1, n) + \
           solution(sum+2, n) + \
           solution(sum+3, n)


n_test = int(sys.stdin.readline())

for _ in range(n_test):
    N = int(sys.stdin.readline())
    print(solution(0, N))
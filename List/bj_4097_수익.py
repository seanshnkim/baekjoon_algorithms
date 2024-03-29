'''다이나믹 프로그래밍을 이용하면 쉬운 문제도, DP를 사용하지 않으면 굉장히 어렵게 풀게 될 수도 있음.
왜 디버깅하는 데만 한시간 반이 걸렸을까?'''

import sys

answers = []
while N := int(input()):
    profit_list = []
    for _ in range(N):
        profit_list.append(int(sys.stdin.readline()))

    max_sum = curr_sum = -10001 

    for p in profit_list:
        # if curr_sum > 0 and p > 0:
        if curr_sum < p and curr_sum < 0:
            curr_sum = p
            if curr_sum > max_sum:
                max_sum = curr_sum
        elif p > 0:
            curr_sum += p
            if curr_sum > max_sum:
                max_sum = curr_sum
        else:
            curr_sum += p
    print(max_sum)

'''
max_sum = 0
min_sum = sys.maxsize

for n in profit_list:
    min_sum = min(min_sum, n)
    max_sum = max(max_sum, n - min_sum)

answers.append(max_sum)
'''
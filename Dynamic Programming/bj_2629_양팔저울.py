import sys
input = sys.stdin.readline
from itertools import accumulate

N_weight = int(input())
# 오름차순 정렬되어 있다
weights = list(map(int, input().split()))
sum_weights = sum(weights)
acc_sum_weights = list(accumulate(weights))

N_marble = int(input())
marbles = list(map(int, input().split()))

# dp[n][w] = V -> 0~n번째 weight를 사용하여 무게 합 w를 만들 수 있는 경우의 수 V
dp = [[False]*(sum_weights+1) for _ in range(N_weight)]
dp[0][0] = True
dp[0][weights[0]] = True

acc_sum = weights[0]
for i in range(1, N_weight):
    cur_w = weights[i]
    for w in range(acc_sum+1):
        if dp[i-1][w]:
            dp[i][w] = True
            dp[i][w+cur_w] = True

            if w - cur_w >= 0:
                dp[i][w - cur_w] = True
            if cur_w - w >= 0:
                dp[i][cur_w - w] = True
                
    acc_sum += cur_w

answers = []
for marble in marbles:
    if marble > sum_weights:
        answers.append('N')
    else:
        if dp[-1][marble]:
            answers.append('Y')
        else:
            answers.append('N')

print(' '.join(answers))

'''
2
1 4
2
3 2

추가 1,4 이면, 
3 -> 4-1=3
2 -> 4와 1 가지고는 만들 수 없다

4
2 3 3 3
3
1 4 10
추가 2,3,3,3이면,
1 -> 3-2 = 1
4 -> 3+3-2 = 4
10 -> NO

'''
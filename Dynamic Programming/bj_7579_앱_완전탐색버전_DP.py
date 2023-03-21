import sys
input = sys.stdin.readline
from itertools import accumulate

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
sum_costs = sum(costs)
mem_costs = [(costs[i], memories[i]) for i in range(N)]
mem_costs.sort(key=lambda x: (x[0], x[1]))
acc_sum_costs = list(accumulate(x[0] for x in mem_costs))

# dp 배열에는 memory (앱 메모리)가 담겨있어야 함
dp = [0]*(sum_costs+1)

for i in range(N):
    cost, mem = mem_costs[i]
    
    for c in range(cost, acc_sum_costs[i]+1):
        if dp[c] == 0 or (dp[c] < dp[c-cost] + mem):
            if cost == 0:
                # dp[c] = mem이 아니다
                dp[c] += mem
            elif dp[c-cost] > 0 or c == cost:
                dp[c] = dp[c-cost] + mem
            
            '''
            5 60
            30 10 20 35 40
            3 0 3 5 4
            처음엔 cost = 0, acc_sum_costs[i] = 0
            dp[0] -> 10
            dp[1]
            '''

for c in range(sum_costs):
    if dp[c] >= M:
        print(c)
        break

'''
dp[0] = 
dp[3] = 20
==========
dp[6] = 40
==========
dp[7] = 60
dp[10] = 100
==========
dp[5] = 80
dp[8] = 100
dp[9] = 120
dp[12] = 120

'''

'''
5 60
30 10 20 35 40
3 0 3 5 4
0 -> (0, 10) 만 쓸 수 있다
0~3 -> ()
3~6
6~10
10~15

-> 정렬하면
(0, 10)
(3, 20)
(3, 30)
(4, 40)
(5, 35)

-> 최소 비용(비활성화 메모리)을 기준으로 dp 저장? -> 
예) dp[6] = 비활성화 메모리 값을 6으로 만들 수 있는 방법 중 활성화 메모리 값

하나 사용한 경우, 둘 사용한 경우

M = 60
처음에는
(0, 10)
(3, 20)
(3, 30)
(4, 40)
(5, 35)

그 다음에
(0, 10) + (3, 20) -> (3, 30)
(0, 10) + (3, 30) -> (3, 40)
(0, 10) + (4, 40) -> (4, 50)
(0, 10) + (5, 35) -> (5, 45)

그 다음에
(3, 20) + (3, 30) -> (6, 50)
(3, 20) + (4, 40) -> (7, 60) -> 만족, 중단?
(3, 20) + (5, 35) -> (8, 55)

그 다음에
(3, 30) + (4, 40) -> (7, 70)
(3, 30) + (5, 35) -> (8, 65)
(3, 30) + (5, 35) -> (8, 65)

(4, 40) + 


반례 2)
N = 4, M = 80
20 20 40 80  
3  3  4  5  
내 풀이가 잘못되었다.

1개만 쓴 경우 (여기선 M = 대충 한 120이라 생각하자)
(3, 20)
(3, 20)
(4, 40)
(5, 80)

2개를 쓴 경우
if dp[][1] (메모리 값) >= M:
    break
else:
    dp[][1] (메모리 값) + 현재 메모리 값
    그렇게 해서 더한 결과가 M 이상이면,
    비활성 메모리를...
    
(3, 20) + (3, 20) -> (6, 40)
(3, 20) + (4, 40) -> (7, 60)
(3, 20) + (5, 80) -> (8, 100)
(3, 20) + (4, 40) -> (7, 60)
(3, 20) + (5, 80) -> (8, 100)
(4, 40) + (5, 80)

비트마스크를 활용해서 하면... N = 100일 땐 2 << 100 -> 감당 안되는 숫자다.

'''


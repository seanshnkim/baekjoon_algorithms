import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memories = list(map(int, input().split()))
inact_mem = list(map(int, input().split()))
mem_tuples = [(inact, mem) for inact, mem in zip(inact_mem, memories)]
# 비활성화 메모리를 기준으로 오름차순 정렬
mem_tuples.sort(key=lambda x: (x[0], x[1]))

dp = [0]*N
dp[0] = mem_tuples[0][0]

answer = dp[0]
for i in range(1, N):
    dp[i] = dp[i-1] + mem_tuples[i][1]
    answer += mem_tuples[i][0]
    if dp[i] >= M:
        break
    
print(answer)

'''
5 60
30 10 20 35 40
3 0 3 5 4

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

'''


import sys
input = sys.stdin.readline
import heapq

'''
4
40 30 30 50
'''

T = int(input())
for t in range(T):
    K = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    total_sum = 0
    for k in range(K-1, 0, -1):
        min1 = heapq.heappop(numbers)
        min2 = heapq.heappop(numbers)
        cur_sum = min1 + min2
        
        if k == K-1:
            # 문제에서 K( len(numbers), 또는 len(dp[K]) ) >= 3. pop 연산 예외처리 X
            # dp[k][0] = 파일이 k개 남아있을 때 만들 수 있는 최소 크기
            total_sum = cur_sum
        else:
            # compare min(dp[k][1:])+dp[k][0] vs. min1 + min2 both from dp[k][1:] 
            # dp[k] 내림차순으로 정렬되어 있다.
            # len(dp[k]) == k. for loop에서 k > 1이므로 IndexError X
            
            # 같을 때도 dp[k][-2] 대신에 dp[k][0] 고르는 게 포인트?
            total_sum += cur_sum
            
        heapq.heappush(numbers, cur_sum)
    
    print(total_sum)
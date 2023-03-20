import sys
input = sys.stdin.readline


def dfs(i, inact_mem, mem):
    global answer
    
    if i == N or mem >= M:
        return
    # or (dp[sum_mem] != -1 and inact_mem >= dp[sum_mem])
    sum_mem = mem + memories[i]
    sum_inact = inact_mem + inact_memories[i]
    # 더 이상 dp 배열 업데이트의 의미가 없으므로 불필요한 계산 중단
    
    if sum_mem >= M:
        sum_mem = M
    if dp[sum_mem] == -1 or dp[sum_mem] > sum_inact:
        dp[sum_mem] = sum_inact

    # memories[i]를 더하지 않는 경우
    dfs(i+1, inact_mem, mem)
    if dp[M] != -1 and sum_inact >= dp[M]:
        return
    dfs(i+1, dp[sum_mem], sum_mem)


N, M = map(int, input().split())
memories = list(map(int, input().split()))
inact_memories = list(map(int, input().split()))
dp = [-1]*(M+1)

dfs(0, 0, 0)

print(dp[M])



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


import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums = list(set(nums))
nums.sort()

while nums[-1] > K:
    nums.pop()

dp = [-1]*(K+1)

len_nums = len(nums)
for cur_num in nums:
    dp[cur_num] = 1
    for j in range(cur_num+1, K+1):
        if dp[j-cur_num] != -1:
            if dp[j] == -1 or dp[j] > dp[j-cur_num] + 1:
                dp[j] = dp[j-cur_num] + 1
    
print(dp[K])
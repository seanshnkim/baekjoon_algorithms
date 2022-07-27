# 2022-06-25(June 25th, 2022), Sehyun Kim

dp = {1:0, 2:1}

def find(n):
    if n in dp:
        return dp[n]
    
    x = find(n//2) + n%2
    y = find(n//3) + n%3
    
    m = 1 + min(x, y)
    # python의 dictionary는 n번째 index로 indexing하는 게 아니라 key 값 그 자체로 찾아내는 것
    dp[n] = m
    return m

n = int(input())
print(find(n))
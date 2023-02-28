import sys
input = sys.stdin.readline

def preprocessing(pattern):
    m = len(pattern)
    pi = [0]*m
    j = 0
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        
        if pattern[i] == pattern[j]:
            pi[i] = j+1
            j += 1
        else:
            pi[i] = 0
    return pi
        

def kmp(given_str, pattern):
    pi = preprocessing(pattern)
    ans = []
    
    n = len(given_str)
    m = len(pattern)
    
    i = j = 0
    
    for i in range(n):
        while j > 0 and given_str[i] != pattern[j]:
            j = pi[j-1]
        
        if given_str[i] == pattern[j]:
            if j == m-1:
                ans.append(i-m+1)
                j = pi[j]
            else:
                j += 1
    return ans
    

given_str = input().rstrip('\n')
pattern = input().rstrip('\n')
matched = kmp(given_str, pattern)

cnt = len(matched)
print(cnt)
if cnt > 0:
    print(' '.join(map(lambda x: str(x+1), matched)))
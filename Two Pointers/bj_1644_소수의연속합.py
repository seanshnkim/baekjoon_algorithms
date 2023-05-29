import sys
input = sys.stdin.readline

N = int(input())
arr = [True]*(N+1)
primes = []

for i in range(2, N+1):
    if arr[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            arr[j] = False

left, right = 0, 0
cur_sum = 0
ans = 0
len_prime = len(primes)

while True:
    if cur_sum >= N:
        if cur_sum == N:
            ans += 1
            
        cur_sum -= primes[left]
        left += 1
        
    elif right == len_prime:
        break
    
    else:
        cur_sum += primes[right]
        right += 1

print(ans)
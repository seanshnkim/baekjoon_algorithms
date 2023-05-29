import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [True]*(N+1)
primes = []

for i in range(2, N+1):
    if arr[i]:
        if i >= M:
            primes.append(i)
        for j in range(2*i, N+1, i):
            arr[j] = False

print(*primes)
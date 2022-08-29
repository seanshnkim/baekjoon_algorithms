import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    num_list = [int(input()) for _ in range(N)]
    
    for i in range(1, N):
        num_list[i] = max(num_list[i], num_list[i-1] + num_list[i])
    print(max(num_list))
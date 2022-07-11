from itertools import accumulate

n = int(input())

numList= list(map(int, input().split()))

print(sum(accumulate(sorted(numList))))
from sys import stdin
from collections import Counter

def BS_Tree(data,m):
    start, end = 0, max(data)
    answer = 0
    while start <= end:
        mid = (start + end) //2
        result = 0
        for item, num in data.items():
            if item > mid:
                result += (item-mid) * num
        if result >= m:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer

n, m = map(int, stdin.readline().split())
data = Counter(map(int, stdin.readline().split()))
print(BS_Tree(data, m))
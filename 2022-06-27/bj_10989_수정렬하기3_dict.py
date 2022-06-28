n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

dict = {}
for num in arr:
    if num in dict.keys():
        dict[num] += 1
    else:
        dict[num] = 1


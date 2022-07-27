# 2022-06-27(June 27th, 2022), Sehyun Kim

num = int(input())
numList = list(map(int, input().split()))

cache_acc = [0 for i in range(num)]

cache_acc[0] = max_acc = numList[0]
for n in range(1, num):
    currNum = numList[n]
    cache_acc[n] = cache_acc[n-1] + currNum
    
    if cache_acc[n] < currNum:
        cache_acc[n] = currNum
    
    if cache_acc[n] > max_acc:
        max_acc = cache_acc[n]

print(max_acc)






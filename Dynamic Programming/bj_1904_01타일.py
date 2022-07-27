# 2022-06-27(June 27th, 2022), Sehyun Kim

cache = [0 for i in range(1000001)]
cache[1] = 1
cache[2] = 2

# def tile(n):
#     if cache[n] != 0:
#         return cache[n]
#     cache[n] = tile(n-1) + tile(n-2)
#     return cache[n]


num = int(input())

for n in range(3, num+1):
    cache[n] = cache[n-1] + cache[n-2]
    cache[n] %= 15746

print(cache[num])


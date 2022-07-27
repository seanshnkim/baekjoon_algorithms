# 2022-06-27(June 27th, 2022), Sehyun Kim

numTestCase = int(input())

cache = [0 for i in range(101)]
cache[1] = cache[2] = cache[3] = 1
cache[4] = cache[5] = 2

#  # cache[4] = 2
# cache[4] = cache[1] + cache[3]
# # cache[5] = 2
# cache[5] = cache[4]
# # cache[6] = 3
# # cache[6] = cache[1] + cache[5]
# cache[6] = cache[3] + cache[5]
# # cache[7] = 4
# cache[7] = cache[2] + cache[6]
# # cache[8] = 5
# # cache[8] = cache[3] + cache[7]
# cache[8] = cache[1] + cache[7]
# # cache[9] = 7
# cache[9] = cache[4] + cache[8]
# # cache[10] = 9
# cache[10] = cache[5] + cache[9]
# # cache[10] = 10
# cache[11] = cache[6] + cache[10]


for t in range(numTestCase):
    num = int(input())

    if num <= 5:
        print(cache[num])
    else:
        if cache[num] == 0:
            for n in range(6, num+1):
                cache[n] = cache[n-5] + cache[n-1]
        print(cache[num])
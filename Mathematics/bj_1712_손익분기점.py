# 2022-06-25(June 25th, 2022), Sehyun Kim

import math

if __name__ == '__main__':
    invarPrice, varPrice, sellPrice = map(int, input().split())

    if sellPrice <= varPrice:
        print(-1)
    else:
        print(math.floor(invarPrice / (sellPrice - varPrice)) + 1)
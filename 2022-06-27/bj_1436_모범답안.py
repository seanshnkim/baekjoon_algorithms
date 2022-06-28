# 장점: 코드가 간결하다
# 단점: 832ms(파이썬 코드로 짠 1~10등 풀이는 60ms 내외)
N = int(input())

first = 666

while N != 0:
    if '666' in str(first):
        N -= 1
        if N == 0:
            break
    first = first + 1
print(first)
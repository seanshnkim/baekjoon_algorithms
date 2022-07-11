n = int(input())

# list의 길이를 input 변수로 설정하면 느려지나?
# dp_table = [0 for i in range(n+1)]
dp_table = [0 for i in range(1001)]
dp_table[1] = 1
dp_table[2] = 2

if n > 2:
    for i in range(3,n+1):
        dp_table[i] = (dp_table[i-1] + dp_table[i-2]) % 10007

print(dp_table[n])
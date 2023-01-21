
ans = []
while True:
    try:
        n = int(input())
    except:
        break
    
    if n == 1:
        ans.append(1)
    else:
        digit = remainder = i = 1
        while True:
            remainder += (10**i % n)
            remainder %= n
            digit += 1
            i += 1
            if remainder == 0:
                ans.append(digit)
                break

for d in ans:
    print(d)
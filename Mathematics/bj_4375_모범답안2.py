ans = []
while True:
    try:
        n = int(input())
    except:
        break
    
    if n == 1:
        ans.append(1)
    else:
        remainder = digit = 1
        
        while True:
            remainder = (remainder * 10) + 1
            remainder %= n
            digit += 1
            if remainder == 0:
                ans.append(digit)
                break

for d in ans:
    print(d)
    
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
        def_rem = 10 % n
        
        while True:
            remainder = (remainder * def_rem) % n + 1
            remainder %= n
            digit += 1
            if remainder == 0:
                ans.append(digit)
                break

for d in ans:
    print(d)



    
# 2022-06-25(June 25th, 2022), Sehyun Kim

inputNum=input()
lenNum, inputInt = len(inputNum), int(inputNum)

start = 0 if inputInt - 9*lenNum < 0 else inputNum - 9*lenNum
end = 1 if inputInt - lenNum == 0 else inputInt - lenNum
result = 0

for i in range(start, end+1):
    num = f'{i}'
    numSum = 0
    for j in range(len(num)):
        numSum += int(num[j])
    if i + numSum == inputInt:
        result = i
        break
    
print(result)
nTypeCoin, value = map(int, input().split())

coinList = []
for i in range(nTypeCoin):
    coinList.append(int(input()))

currVal = value
cnt = 0
# 매번 뺄셈을 수행하는 건 시간이 너무 오래 걸린다(시간 초과로 실패)
# for i in reversed(range(nTypeCoin)):
#     if currVal == 0:
#         break

#     currCoin = coinList[i]

#     while currVal >= currCoin:
#         currVal -= currCoin
#         cnt += 1

for i in reversed(range(nTypeCoin)):
    currCoin = coinList[i]
    if currVal >= currCoin:
        cnt += currVal // currCoin
        currVal = currVal % currCoin
        if currVal == 0:
            break

print(cnt)

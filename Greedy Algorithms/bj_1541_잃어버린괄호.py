# 2022-07-03, Sehyun Kim
expr = input()
lenExpr = len(expr)

minusIdx = expr.find('-')
if minusIdx != - 1:
    res = expr[:minusIdx]
else:
    res = expr
res = sum(map(int, res.split('+')))

while minusIdx != -1:
    currIdx = minusIdx
    minusIdx = expr.find('-', currIdx+1)
    if minusIdx == -1:
        subString = expr[currIdx+1:]
    else:
        subString = expr[currIdx+1 : minusIdx]

    toSubtract = sum(map(int, subString.split('+')))
    res -= toSubtract

print(res)
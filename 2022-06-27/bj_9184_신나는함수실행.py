# 이 방식으로 배열을 선언하면 안 되는 이유: https://www.acmicpc.net/board/view/79184
# cache = [[[-1] * 21]*21] * 21

cache = [[[-1] * 21 for i in range(21)] for j in range(21)]

def recur(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x > 20 or y > 20 or z > 20:
        if cache[20][20][20] != -1:
            return cache[20][20][20]

        cache[20][20][20] = recur(20, 20, 20)
        return cache[20][20][20]

    if x < y and y < z:
        if cache[x][y][z] != -1:
            return cache[x][y][z]

        if cache[x][y][z-1] == -1:
            cache[x][y][z-1] = recur(x, y, z -1)

        if cache[x][y-1][z-1] == -1:
            cache[x][y-1][z-1] = recur(x, y-1, z-1)
        
        if cache[x][y-1][z] == -1:
            cache[x][y-1][z] = recur(x, y-1, z)

        return cache[x][y][z-1] +  cache[x][y-1][z-1] - cache[x][y-1][z]

    else:
        if cache[x][y][z] != -1:
            return cache[x][y][z]
        
        if cache[x-1][y][z] == -1:
            cache[x-1][y][z] = recur(x-1, y, z)

        if cache[x-1][y-1][z] == -1:
            cache[x-1][y-1][z] = recur(x-1, y-1, z)

        if cache[x-1][y][z-1] == -1:
            cache[x-1][y][z-1] = recur(x-1, y, z-1)
        
        if cache[x-1][y-1][z-1] == -1:
            cache[x-1][y-1][z-1] = recur(x-1, y-1, z-1)

        return cache[x-1][y][z] + cache[x-1][y-1][z] + cache[x-1][y][z-1] - cache[x-1][y-1][z-1]

a, b, c = 0, 0, 0
answerList = []
abcList = []
while(not (a == -1 and b == - 1 and c == -1)):
    a, b, c = map(int, input().split())
    abcList.append((a,b,c))
    answerList.append(recur(a, b, c))

numAns = len(answerList)
for i in range(numAns):
    print(f'w({abcList[i][0]}, {abcList[i][1]}, {abcList[i][2]}) = {answerList[i]}')

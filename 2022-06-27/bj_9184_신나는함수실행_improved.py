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

    if cache[x][y][z] != -1:
        return cache[x][y][z]

    toAdd = [(0,0,-1), (0,-1,-1), (0,-1,0), (-1,0,0), (-1,-1,0), (-1,0,-1), (-1,-1,-1)]
    ans = 0

    for i in range(7):
        a,b,c = map(sum, zip((x,y,z),toAdd[i]))

        if cache[a][b][c] == -1:
            cache[a][b][c] = recur(a, b, c)
        
        if i == 3:
            ans = cache[a][b][c]

        elif (x < y and y < z and i == 2) or i == 6:
            ans -= cache[a][b][c]
            break
        else:
            ans += cache[a][b][c]
    return ans

a, b, c = 0, 0, 0
answerList = []
abcList = []

# 이렇게 하면 (a,b,c) == (-1,-1,-1)일 때에도 a,b,c에 값이 저장된다.
# while(not (a == -1 and b == - 1 and c == -1)):
while(True):
    a, b, c = map(int, input().split())
    
    if (a == -1 and b == - 1 and c == -1):
        break

    abcList.append((a,b,c))
    answerList.append(recur(a, b, c))

numAns = len(answerList)
for i in range(numAns):
    print(f'w({abcList[i][0]}, {abcList[i][1]}, {abcList[i][2]}) = {answerList[i]}')



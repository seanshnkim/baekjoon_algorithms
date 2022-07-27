# 2022-06-27(June 27th, 2022), Sehyun Kim

height, width = map(int, input().split())

chessBoard_white = []
chessBoard_black = []
for i in range(4):
    chessBoard_white += ['WBWBWBWB', 'BWBWBWBW']
    chessBoard_black += ['BWBWBWBW', 'WBWBWBWB']

givenBoard = []
for _ in range(height):
    givenBoard.append(input())

minCnt = 64
Wcnt, Bcnt = 0, 0
for hStart in range(height-7):
    for wStart in range(width-7):
        Wcnt, Bcnt = 0, 0
        for h in range(8):
            for w in range(8):
                if givenBoard[hStart + h][wStart + w] != chessBoard_white[h][w]:
                    Wcnt += 1
                if givenBoard[hStart + h][wStart + w] != chessBoard_black[h][w]:
                    Bcnt += 1
        curMinCnt = min(Wcnt, Bcnt)
        if curMinCnt < minCnt:
            minCnt = curMinCnt

print(minCnt)

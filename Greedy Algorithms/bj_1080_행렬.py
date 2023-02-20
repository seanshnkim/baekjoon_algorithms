import sys
input = sys.stdin.readline

ROW, COL = map(int, input().split())

A = [[int(s) for s in input().rstrip('\n')] for _ in range(ROW)]
B = [[int(s) for s in input().rstrip('\n')] for _ in range(ROW)]


def invert_matrix(input_matrix, start_r, start_c):
    for r in range(start_r, start_r+3):
        for c in range(start_c, start_c+3):
            input_matrix[r][c] ^= 1


def solution():
    answer = 0
    
    if ROW < 3 or COL < 3:
        for r in range(ROW):
            if A[r] != B[r]:
                return -1
    
    for r in range(0, ROW-2):
        for c in range(0, COL-2):
            if A[r][c] != B[r][c]:
                invert_matrix(A, r, c)
                answer += 1
                
        for cc in range(COL-2, COL):
            if A[r][cc] != B[r][cc]:
                return -1
    
    for rr in range(ROW-2, ROW):
        if A[rr] != B[rr]:
            return -1
    
    return answer

print(solution())

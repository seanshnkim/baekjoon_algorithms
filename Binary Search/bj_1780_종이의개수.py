import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

counts = {-1: 0, 0: 0, 1:0}

# row_s -> start point(row)
# col_s -> start point(col)
# length -> length of current matrix(size = k*k, k = 3^i )
def solution(row_s, col_s, length):
    if length == 1:
        counts[matrix[row_s][col_s]] += 1
        return
    
    first = matrix[row_s][col_s]
    for r in range(row_s, row_s+length):
        for c in range(col_s, col_s+length):
            curr = matrix[r][c]
            if first != curr:
                l = length // 3
                for rr in range(3):
                    for cc in range(3):
                        solution(row_s+rr*l, col_s+cc*l, l)
                return
            
    counts[first] += 1
    return

solution(0, 0, N)
print(counts[-1])
print(counts[0])
print(counts[1])
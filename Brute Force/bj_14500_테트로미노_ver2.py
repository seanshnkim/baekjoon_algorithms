import sys
from itertools import combinations

width, length = map(int, sys.stdin.readline().split())

arr_2D = []
for w in range(width):
    arr_2D.append(list(map(int, sys.stdin.readline().split())))

# width down   --> + (1,0)
# length right --> + (0,1)
tetrominos = [
    # O O O O
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    # O O
    # O O
    [(0,0), (0,1), (1,0), (1,1)],
    # O O O
    #     O
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,2), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(0,1), (1,1), (2,1), (2,0)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (1,0), (1,1), (1,2)],
    # O
    # O O
    #   O
    [(0,0), (1,0), (1,1), (2,1)],
    [(0,1), (0,2), (1,0), (1,1)],
    [(0,0), (0,1), (1,1), (1,2)],
    [(0,1), (1,0), (1,1), (2,0)],
    # O O O
    #   O
    [(0,0), (1,0), (1,1), (2,0)],
    [(0,1), (1,0), (1,1), (1,2)],
    [(0,1), (1,1), (2,1), (1,0)],
    [(0,0), (0,1), (0,2), (1,1)],
]


max_sum = sum_nums = 4

for w in range(width):
    for l in range(length):
        pt = (w, l)
        for tetromino in tetrominos:
            is_in_arr_2D = True
            
            # get real coords:
            cord_tetrominos = [(pt[0] + t[0], pt[1] + t[1]) for t in tetromino]
            
            for cord in cord_tetrominos:
                if cord[0] >= width or cord[1] >= length:
                    is_in_arr_2D = False
                    break
            if is_in_arr_2D:
                sum_nums = sum(arr_2D[a][b] for (a,b) in cord_tetrominos)
                max_sum = max(max_sum, sum_nums)

print(max_sum)
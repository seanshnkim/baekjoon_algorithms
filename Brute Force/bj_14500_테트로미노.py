import sys
from itertools import combinations

width, length = map(int, sys.stdin.readline().split())

arr_2D = []
for w in range(width):
    arr_2D.append(list(map(int, sys.stdin.readline().split())))
    
    
def is_tetromino(list_coords):
    for coord in list_coords:
        up =    (coord[0] - 1, coord[1])
        down =  (coord[0] + 1, coord[1])
        left =  (coord[0], coord[1] - 1)
        right = (coord[0], coord[1] + 1)
        
        surroundings = [up, down, left, right]
        not_adj = 0
        for surr in surroundings:
            if surr not in list_coords:
                not_adj += 1
        if not_adj == 4:
            return False
        
    return True

max_sum = 4
for comb in combinations(range(width*length), 4):
    # comb --> 4 different numbers ranging from [0, width*length)
    list_coords = [(num//length, num%length) for num in comb]
    
    if is_tetromino(list_coords):
        sum = 0
        for (w, l) in list_coords:
            sum += arr_2D[w][l]
        max_sum = max(max_sum, sum)
    
    